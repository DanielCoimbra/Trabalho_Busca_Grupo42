# Trabalho_Busca_Grupo42

### Trabalho 01 - 27/11/2025

## Aluno 
| Matrícula | Nome |  
|-----------------------|---------------------|  
| 18/0113097 | Daniel Coimbra dos Santos |  

## Descrição do projeto
Resolução de questões do LeetCode para demonstrar na prática os conhecimentos adquiridos acerca do conteúdo Algoritmos de Busca
### Questão de Dificuldade Difícil:
#### 749. Contain Virus
Hard
Topics
premium lock icon
Companies
Hint
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

Example 1:

<img width="653" height="333" alt="image" src="https://github.com/user-attachments/assets/ae13cb7e-3625-46ae-9b48-19b304bd9445" />

Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
<img width="653" height="335" alt="image" src="https://github.com/user-attachments/assets/6bbdf4c1-5a60-4334-b46b-ce99e3d8ba04" />

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
<img width="653" height="341" alt="image" src="https://github.com/user-attachments/assets/ee142c83-9cdd-44c7-83de-86e954ef7219" />

Example 2:

<img width="653" height="253" alt="image" src="https://github.com/user-attachments/assets/0d87293a-750c-4ec1-841c-a09686d9d1df" />

Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:

Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
 

Constraints:

m == isInfected.length
n == isInfected[i].length
1 <= m, n <= 50
isInfected[i][j] is either 0 or 1.
There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.

## Capturas de tela
<p>Pancake Sorting - Questão e Código</p><img src="imgs/contain_virus.PNG"><br>
<br>
<p>Runtime Metrics</p><img src="imgs/runtime_contain_virus.PNG"><br>
<p>Runtime Metrics</p><img src="imgs/memory_contain_virus.PNG"><br>

## Conclusões

O algoritmo do Contain Virus funciona como uma simulação iterativa. A cada “dia”, ele identifica todas as regiões infectadas do grid usando DFS/BFS, calcula quantas células saudáveis cada região ameaça contaminar, escolhe a região mais perigosa e instala paredes ao redor dela. As demais regiões continuam se espalhando, e o processo se repete enquanto houver risco de infecção.

A complexidade vem justamente dessa repetição: cada rodada exige percorrer o grid inteiro, o que custa O(m·n), e várias rodadas podem ocorrer, elevando o custo total. O uso de memória fica em O(m·n), por conta do armazenamento temporário de regiões, fronteiras e marcações de visita.

O método tem a vantagem de seguir exatamente o comportamento descrito no enunciado e ser didático para entender como a propagação funciona. No entanto, ele é relativamente pesado, pois recalcula tudo a cada ciclo e toma decisões sempre de forma gananciosa — ótima localmente, mas não necessariamente globalmente. Mesmo assim, o problema é excelente para estudar busca em ambientes dinâmicos e entender como decisões locais afetam um sistema que muda continuamente.

## Sobre o algoritmo

O Contain Virus é interessante porque combina identificação de componentes conectados por DFS/BFS com uma heurística simples: escolher a região que ameaça mais células na próxima rodada. Essa heurística funciona como uma função de avaliação típica em algoritmos de busca, guiando o algoritmo a conter o vírus onde mais importa.

Como o grid muda a cada ação — seja pela construção de paredes ou pela expansão do vírus — o algoritmo precisa reavaliar o estado constantemente. Isso cria um pequeno processo de planejamento: observar o estado atual, aplicar uma ação que modifica o ambiente e lidar com suas consequências. Por isso, o problema serve como um bom exemplo de busca em sistemas dinâmicos, onde o estado evolui e a solução depende de decisões locais bem fundamentadas.

## Complexidade 

| Etapa | Tempo | Espaço |
|-------|--------|---------|
| Identificação das regiões (DFS/BFS) | O(m·n) | O(m·n) |
| Cálculo das fronteiras | O(m·n) | O(m·n) |
| Construção das paredes | O(t) (t = tamanho da região) | O(1) |
| Propagação do vírus | O(m·n) | O(1) |
| Total por rodada | O(m·n) | O(m·n) |
| Total geral | O(k·m·n) (k = nº de dias/simulações) | O(m·n) |

---

## Grupo
<img src="https://avatars.githubusercontent.com/u/49206670?s=400&u=200e3dc888a00aa86108318d2d9b6c33aa94abe1&v=4" width=150><br>
      <b><a href="https://github.com/DanielCoimbra">Daniel Coimbra</a></b><br>
