Feature: Procura em grafo por Depth First Search

Scenario Outline: Encontrar um caminho em um grafo do arquivo "mini_map.txt" 
Given a descrição de um grafo a partir do arquivo "mini_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com BFS
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   |  7   |   6   | [0, 2, 1, 3, 5, 7] |
    |   0   |  9   |   1   | [0, 9] |
    |   3   |  7   |   4   | [3, 2, 5, 7] |
    |   0   |  6   |   3   | [0, 2, 9, 6] |

Scenario Outline: Encontrar um caminho em um grafo do arquivo "small_map.txt" 
Given a descrição de um grafo a partir do arquivo "small_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com BFS
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   | 764  |  717  | [0, 383, 374, 999, 296, 252, 261, 868, 867, 866, 869, 872, 871, 870, 855, 856, 857, 862, 859, 858, 764] |
    |   230 | 850  |  511  | [230, 231, 243, 281, 227, 228, 302, 999, 296, 252, 261, 868, 867, 866, 869, 872, 871, 870, 855, 850] |
    |   0   |  20  |   84  | [0, 16, 459, 20] |
    |   0   |  6   |   55  | [0, 383, 396, 1, 418, 3, 5, 6] |
