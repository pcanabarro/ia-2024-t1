"""Implementação da busca em profundidade."""

from queue import deque as Queue

from util import reverse_path

from collections import deque

def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    visited = set()
    queue = deque([(start, [start], 0.0)])

    while queue:
        current_node, path, cost = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal:
                return len(path), cost, path

            for neighbor, edge_cost in graph[current_node]['edges']:
                if neighbor not in visited:
                    total_cost = cost + edge_cost
                    queue.append((neighbor, path + [neighbor], total_cost))

    return 0, float('inf'), []