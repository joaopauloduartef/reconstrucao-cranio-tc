import matplotlib.pyplot as plt

def plotar_fatia_e_mascara(fatia_original, fatia_mascara, indice, limiar):
    """Gera um gráfico comparativo entre a imagem real de CT e a segmentação óssea."""
    plt.figure(figsize=(12, 6))
    
    # Imagem médica original em tons de cinza
    plt.subplot(1, 2, 1)
    plt.imshow(fatia_original, cmap='gray')
    plt.title(f"Fatia Original #{indice} (DICOM)")
    plt.axis('off')

    # Filtro de densidade (Unidades Hounsfield - HU)
    plt.subplot(1, 2, 2)
    plt.imshow(fatia_mascara, cmap='gray')
    plt.title(f"Conjunto de Nível (Osso > {limiar} HU)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()