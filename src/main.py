"""Utilize este arquivo para depurar seus algoritmos."""

from graph import read_graph
from busca import a_star, bfs, branch_and_bound, dfs, dijkstra


if __name__ == "__main__":
    # mini_graph = read_graph("../mapas/mini_map.txt")
    micro_graph = read_graph("../mapas/micro_map.txt")
    # small_graph = read_graph("../mapas/small_map.txt")
    # medium_graph = read_graph("../mapas/medium_map.txt")
    # full_graph = read_graph("../mapas/full_map.txt")

    START_VERTEX = 30
    GOAL_VERTEX = 44

    try:
        # path_length, cost, shortest_path = a_star(mini_graph, START_VERTEX, GOAL_VERTEX)  # A* path
        # path_length, cost, shortest_path = bfs(mini_graph, START_VERTEX, GOAL_VERTEX)  # BFS path
        path_length, cost, shortest_path = dfs(micro_graph, START_VERTEX, GOAL_VERTEX)  # DFS path

        print("Comprimento do caminho mais curto", START_VERTEX, "para", GOAL_VERTEX, ":", path_length)
        print("Custo do caminho mais curto:", cost)
        print("Caminho mais curto:", shortest_path)
    finally:
        print('')

    # vertices_avaliados, custo, caminho = bfs(grafo, 0, 9)
    # print(vertices_avaliados, custo, caminho)
