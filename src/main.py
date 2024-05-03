"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import bfs

if __name__ == "__main__":
    mini_graph = read_graph("../mapas/mini_map.txt")
    # micro_graph = read_graph("../mapas/micro_map.txt")
    # small_graph = read_graph("../mapas/small_map.txt")
    # medium_graph = read_graph("../mapas/medium_map.txt")
    # full_graph = read_graph("../mapas/full_map.txt")
    vextex_visited, cost, path = bfs(mini_graph, 0, 8)
    # vertices_avaliados, custo, caminho = a_star(grafo, 1, 100)
    # print(vertices_avaliados, custo, caminho)