"""Implementação da busca em profundidade."""

# from util import reverse_path


def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em profundidade."""
    if goal not in graph:
        raise ValueError("Goal node does not exist in the graph")

    visited = set()
    stack = [(start, [start])]

    while stack:
        (node, path) = stack.pop()

        # If we reach the goal node, return the path
        if node == goal:
            total_distance = sum(graph[path[i]]['edges'][path[i + 1]][1] for i in range(len(path) - 1))
            return len(path) - 1, total_distance, path

        # If the node has not been visited
        if node not in visited:
            print("node", node)
            print("graph espec", graph[node]['edges'])

            visited.add(node)

            # Explore neighbors of the current node
            for neighbor in graph[node]['edges']:
                print('ue', neighbor)
                if neighbor[0] not in visited:
                    stack.append((neighbor[0], path + [neighbor[0]]))

    raise ValueError("Goal node is not reachable from the start node")
