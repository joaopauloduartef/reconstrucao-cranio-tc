# Processamento de Imagens Médicas: Segmentação e Volume 3D de Arquivos DICOM

Este projeto foca na manipulação, processamento computacional e análise geométrica de exames de Tomografia Computadorizada (CT) salvos no formato padrão da medicina (`.dcm` - DICOM). O objetivo é realizar a leitura de múltiplos cortes anatômicos e construir um volume tridimensional coerente. As imagens tridimensionais de tomografia são tratadas computacionalmente como **Tensores (Arrays de 3 dimensões)**. Cada elemento desse tensor é chamado de **Voxel** (a extensão tridimensional de um pixel).

### Desafios Resolvidos pelo Script:
1. **Ordenação no Espaço Real:** Os arquivos brutos de um exame médico podem vir fora de ordem. O algoritmo faz a leitura dos metadados de cabeçalho do arquivo DICOM e ordena cada matriz baseado no atributo `ImagePositionPatient[2]` (a coordenada real Z do paciente dentro da máquina).
2. **Correção de Anisotropia:** O espaçamento entre as fatias do exame (eixo Z) geralmente é diferente do tamanho do pixel horizontal/vertical (eixo X e Y). O script calcula essa proporção e define um fator de correção tridimensional para evitar que a reconstrução final fique distorcida ou achatada.
3. **Segmentação por Conjunto de Nível (Thresholding):** Utilizando matrizes booleanas baseadas nas Unidades Hounsfield (HU) — escala numérica que mede a radiodensidade de tecidos —, aplicamos filtros matemáticos de corte para separar tecidos moles de estruturas ósseas rígidas.

## Tecnologias e Dependências

* **Python 3**
* **PyDICOM:** Biblioteca especializada para decodificação de arquivos médicos padronizados.
* **NumPy:** Utilizado para manipulação rápida de matrizes multidimensionais e empilhamento de tensores.
* **Matplotlib & Plotly:** Ferramentas gráficas para renderização de cortes e projeções de superfície.