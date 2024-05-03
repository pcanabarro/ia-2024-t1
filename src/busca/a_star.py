"""Implementação do algoritmo A*."""


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""
    open_set = queue()  # Priority queue to store nodes to be explored
    open_set.put((0, start))
    best_cost = {vertex: float('inf') for vertex in graph}
    best_cost[start] = 0
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()

        # If the current node is the goal, reconstruct the path and return
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return len(path), best_cost[goal], path

        # Explore neighbors of the current node
        for neighbor, cost in graph[current]['edges']:
            total_cost = best_cost[current] + cost
            # If the total cost to the neighbor is less than the best known cost so far
            if total_cost < best_cost[neighbor]:
                best_cost[neighbor] = total_cost  # Update the best cost for the neighbor
                open_set.put((total_cost, neighbor))  # Add the neighbor to the priority queue
                came_from[neighbor] = current  # Update the parent node of the neighbor

    return 0, float('inf'), []