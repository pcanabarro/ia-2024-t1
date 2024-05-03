"""Implementação da busca em profundidade."""

from queue import deque as Queue
import collections
# from util import reverse_path


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    visited, queue = set(), collections.deque([start, 0])
    visited.add(start)

    while queue:
        vertex = queue.popleft() # now we have a FIFO queue
        print("Vertex", vertex)
        if vertex == goal:
            # ff goal is found, return the length of path, cost, and the path itself
            return len(path[vertex]), 0, path[vertex]
        print(queue)
        for neighbour in graph:
            print("neighbour", neighbour)
            # print("queue", graph[neighbour]['edges'])
            if neighbour not in visited:
                print(graph[neighbour]['edges'])
                visited.add(neighbour)
                queue.append(graph[neighbour]['edges'])
    print(visited, queue)

    return len(visited), cost, queue