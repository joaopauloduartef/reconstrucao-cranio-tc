from reconstrucao_cranio.processador_dicom import ProcessadorDicom
from reconstrucao_cranio.visualizador import plotar_fatia_e_mascara

def executar_pipeline():
    
    DIRETORIO_DICOM = "dataset/files/aneurysm"
    LIMIAR_OSSO = 300

    print("Iniciando Processamento de Imagens Médicas...")
    processador = ProcessadorDicom(DIRETORIO_DICOM)

    try:
        volume, fator_correcao = processador.carregar_volume()
        print(f"-> Volume 3D carregado com sucesso. Dimensões: {volume.shape}")
        print(f"-> Fator de correção Z calculado: {fator_correcao:.4f}")

        # Pega a fatia central para visualização de teste
        indice_meio = volume.shape[0] // 2
        fatia_original = volume[indice_meio]
        
        # Aplica a segmentação baseada na densidade do osso
        mascara_completa = processador.aplicar_threshold(LIMIAR_OSSO)
        fatia_mascara = mascara_completa[indice_meio]

        print("-> Gerando visualização gráfica da fatia de controle...")
        plotar_fatia_e_mascara(fatia_original, fatia_mascara, indice_meio, LIMIAR_OSSO)
        
        print("\nEtapa 1 Concluída perfeitamente!")

    except Exception as e:
        print(f"\n[ERRO no Pipeline]: {e}")

if __name__ == "__main__":
    executar_pipeline()