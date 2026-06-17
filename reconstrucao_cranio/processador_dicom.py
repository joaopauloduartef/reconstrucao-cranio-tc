import os
import numpy as np
import pydicom

class ProcessadorDicom:
    def __init__(self, diretorio_dados):
        self.diretorio = diretorio_dados
        self.volume = None
        self.fator_z_real = 1.0

    def carregar_volume(self):
        """
        Lê os arquivos DICOM (.dcm), ordena as fatias pela posição Z real
        e calcula o fator de correção de anisotropia dos pixels.
        """
        if not os.path.exists(self.diretorio):
            raise FileNotFoundError(f"Diretório não encontrado: {self.diretorio}")

        arquivos = [f for f in os.listdir(self.diretorio) if f.endswith('.dcm')]
        if not arquivos:
            raise FileNotFoundError("Nenhum arquivo .dcm encontrado no diretório.")

        # Carrega os metadados DICOM
        fatias_dicom = [pydicom.dcmread(os.path.join(self.diretorio, f)) for f in arquivos]

        # Ordena as fatias tridimensionalmente pela posição do paciente no eixo Z
        fatias_dicom.sort(key=lambda x: float(x.ImagePositionPatient[2]))

        # Cálculo da anisotropia espacial (relação de aspecto real do voxel)
        z1 = fatias_dicom[0].ImagePositionPatient[2]
        z2 = fatias_dicom[1].ImagePositionPatient[2]
        espessura_z = abs(z2 - z1)

        pixel_x = fatias_dicom[0].PixelSpacing[0]
        self.fator_z_real = espessura_z / pixel_x

        # Empilha as matrizes 2D para formar um Tensor/Volume 3D
        self.volume = np.stack([s.pixel_array for s in fatias_dicom])
        
        return self.volume, self.fator_z_real

    def aplicar_threshold(self, limiar_hu=300):
        """Aplica o método de conjunto de nível (Thresholding) para segmentar tecidos densos (ossos)."""
        if self.volume is None:
            raise ValueError("O volume de dados não foi carregado.")
        return self.volume > limiar_hu