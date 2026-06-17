from reconstrucao_cranio.processador_dicom import ProcessadorDicom
from reconstrucao_cranio.visualizador import plotar_fatia_e_mascara
from reconstrucao_cranio.gerador_malha import GeradorMalha

def executar_pipeline():
    # Ajuste para a pasta correta no seu VS Code
    DIRETORIO_DICOM = "dataset/files/aneurysm"
    LIMIAR_OSSO = 300

    print("Iniciando Processamento de Imagens Médicas...")
    processador = ProcessadorDicom(DIRETORIO_DICOM)

    try:
        volume, fator_correcao = processador.carregar_volume()
        print(f"-> Volume 3D carregado com sucesso. Dimensões: {volume.shape}")
        print(f"-> Fator de correção Z calculado: {fator_correcao:.4f}")

        # Pega a fatia central para visualização 2D de teste
        indice_meio = volume.shape[0] // 2
        fatia_original = volume[indice_meio]
        
        # Aplica a segmentação baseada na densidade do osso
        mascara_completa = processador.aplicar_threshold(LIMIAR_OSSO)
        fatia_mascara = mascara_completa[indice_meio]

        print("-> Gerando visualização gráfica da fatia de controle (2D)...")
        plotar_fatia_e_mascara(fatia_original, fatia_mascara, indice_meio, LIMIAR_OSSO)
        
        # --- AQUI ENTRA A PARTE DO MARCHING CUBES ---
        GeradorMalha.plotar_volume_3d(volume, LIMIAR_OSSO, fator_correcao)
        
        print("\nPipeline 3D Concluído perfeitamente!")

    except Exception as e:
        print(f"\n[ERRO no Pipeline]: {e}")

if __name__ == "__main__":
    executar_pipeline()