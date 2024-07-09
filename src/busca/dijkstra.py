"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heappush, heappop
from ..util import get_neighbors


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""
    queue = [(0, start, [start])]
    visited = set()
    best = ()

    while queue:
        cost, node, path = heappop(queue)

        if node == goal:
            if not best or best[1] > cost:
                best = (len(path), cost, path)

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in get_neighbors(graph, node):
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    heappush(queue, (new_cost, neighbor, new_path))

    if best:
        path_length, cost, shortest_path = best
        return path_length, cost, shortest_path

    return 0, float('inf'), []
