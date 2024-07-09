"""Implementação do algoritmo 'branch and bound'."""
from collections import deque

def get_neighbors(graph, node):
    """Return neighbors from a node."""
    return graph.get(node, [])

def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando Branch and Bound."""
    visited = set()
    queue = deque([(0, 0, [start])])
    best = (None, None, None)

    while queue:
        # Ordenar pelo custo acumulado (x[1])
        queue = deque(sorted(queue, key=lambda x: x[1]))
        cost, _, current_path = queue.popleft()
        node = current_path[-1]

        if node == goal:
            if best[1] is None or cost < best[1]:
                best = (len(current_path), cost, current_path)

        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(graph, node)

            for neighbor_info in neighbors:
                try:
                    neighbor, edge_cost = neighbor_info
                except ValueError:
                    print(f"Incorrect neighbor info format: {neighbor_info}")
                    continue

                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    if best[1] is None or new_cost < best[1]:
                        new_path = current_path + [neighbor]
                        queue.append((new_cost, new_cost, new_path))

    if best[1] is not None:
        path_length, total_cost, shortest_path = best
        return path_length, total_cost, shortest_path

    return 0, float('inf'), []
