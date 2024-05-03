"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star, bfs, branch_and_bound, dfs, dijkstra

if __name__ == "__main__":
    mini_graph = read_graph("../mapas/mini_map.txt")
    start_vertex = 1
    goal_vertex = 4
    path_length, cost, shortest_path = a_star(mini_graph, start_vertex, goal_vertex)
    print("Comprimento do caminho mais curto de", start_vertex, "para", goal_vertex, ":", path_length)
    print("Custo do caminho mais curto:", cost)
    print("Caminho mais curto:", shortest_path)
    # micro_graph = read_graph("../mapas/micro_map.txt")
    # small_graph = read_graph("../mapas/small_map.txt")
    # medium_graph = read_graph("../mapas/medium_map.txt")
    # full_graph = read_graph("../mapas/full_map.txt")
    # vertices_avaliados, custo, caminho = bfs(grafo, 0, 9)
    # print(vertices_avaliados, custo, caminho)