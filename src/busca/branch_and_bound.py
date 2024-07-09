"""Implementação do algoritmo 'branch and bound'."""
from collections import deque
from ..util import get_neighbors


def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando Branch and Bound."""
    visited = set()
    queue = deque([(0, 0, [start])])
    best = None

    while queue:
        # Ordenar pelo custo acumulado (x[1])
        queue = deque(sorted(queue, key=lambda x: x[1]))
        cost, _, current_path = queue.popleft()
        node = current_path[-1]

        if node == goal:
            if best is None or cost < best[1]:
                best = (len(current_path), cost, current_path)

        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(graph, node)

            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    if best is None or new_cost < best[1]:
                        new_path = current_path + [neighbor]
                        queue.append((new_cost, new_cost, new_path))

    if best:
        path_length, total_cost, shortest_path = best
        return path_length, total_cost, shortest_path

    return 0, float('inf'), []
