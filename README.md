# Projeto de Algoritmos em Grafos
grupo: luis arthur cordeiro e antonio freitas

## Fase 1 – Problemas do LeetCode

### Problema 1: Number of Islands

Algoritmo utilizado: Busca em Profundidade (DFS)

Explicação:
A matriz é tratada como um grafo, onde cada célula representa um nó.
Quando encontramos uma célula com valor "1" (terra), executamos uma DFS para visitar todas as células conectadas que também representam terra. Dessa forma, todas as partes da mesma ilha são marcadas como visitadas e não são contadas novamente.

Complexidade de Tempo: O(m × n)

Complexidade de Espaço: O(m × n)

---

### Problema 2: Course Schedule

Algoritmo utilizado: Busca em Profundidade (DFS) com detecção de ciclo

Explicação:
Os cursos são representados como nós de um grafo e os pré-requisitos são arestas direcionadas entre esses nós.
O algoritmo utiliza DFS para verificar se existe algum ciclo no grafo. Caso exista um ciclo, significa que não é possível concluir todos os cursos, pois um curso dependeria de si mesmo indiretamente.

Complexidade de Tempo: O(V + E)

Complexidade de Espaço: O(V)

---

## Fase 2 – Aplicação no Mundo Real

API utilizada: PokeAPI

Modelagem do Grafo:

Nós: Pokémons
Arestas: Relações de evolução entre Pokémons

Algoritmo utilizado: Busca em Largura (BFS)

Objetivo:
Encontrar o caminho ou relação de evolução entre diferentes Pokémons utilizando dados reais obtidos da API.
