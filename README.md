# Processamento de Imagens Médicas: Segmentação e Reconstrução 3D de Ficheiros DICOM

Este projeto foca na manipulação, processamento computacional e análise geométrica de exames de Tomografia Computorizada (CT) guardados no formato padrão da medicina (`.dcm` - DICOM). O objetivo é realizar a leitura de múltiplos cortes anatómicos e construir um volume tridimensional coerente e navegável. As imagens tridimensionais de tomografia são tratadas computacionalmente como **Tensores (Arrays de 3 dimensões)**. Cada elemento desse tensor é chamado de **Voxel** (a extensão tridimensional de um pixel).

### Desafios Resolvidos pelo Algoritmo:
1. **Ordenação no Espaço Real:** Os ficheiros brutos de um exame médico podem vir fora de ordem. O algoritmo faz a leitura dos metadados de cabeçalho do ficheiro DICOM e ordena cada matriz com base no atributo `ImagePositionPatient[2]` (a coordenada real Z do paciente dentro da máquina).
2. **Correção de Anisotropia:** O espaçamento entre as fatias do exame (eixo Z) geralmente é diferente do tamanho do pixel horizontal/vertical (eixos X e Y). O script calcula essa proporção e define um fator de correção tridimensional para evitar que a reconstrução final fique distorcida ou achatada.
3. **Segmentação por Conjunto de Nível (Thresholding):** Utilizando matrizes booleanas baseadas nas Unidades Hounsfield (HU) — escala numérica que mede a radiodensidade de tecidos —, aplicamos filtros matemáticos de corte para separar tecidos moles de estruturas ósseas rígidas.
4. **Extração de Isosuperfície (Marching Cubes):** Para converter o volume discreto de voxels numa superfície contínua e renderizável, o projeto implementa o algoritmo *Marching Cubes*. Este método divide o espaço 3D em cubos, avalia a densidade nos vértices de cada cubo em relação ao limiar ósseo estabelecido e interpola a criação de polígonos (triângulos), gerando uma malha geométrica de alta fidelidade anatómica.

## Tecnologias e Dependências

* **Python 3**
* **PyDICOM:** Biblioteca especializada para descodificação de ficheiros médicos padronizados.
* **NumPy:** Utilizado para manipulação rápida de matrizes multidimensionais e empilhamento de tensores.
* **Scikit-Image:** Aplicação de algoritmos de geometria computacional (Marching Cubes) para extração da malha 3D.
* **Matplotlib & Plotly:** Ferramentas gráficas para renderização interativa de cortes e projeções de superfície 3D.

