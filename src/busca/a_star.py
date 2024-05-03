"""Implementação do algoritmo A*."""


def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""
    open_set = PriorityQueue()  # Fila de prioridade para armazenar nós a serem explorados
    open_set.put((0, start))  # Adiciona o nó inicial à fila de prioridade
    best_cost = {vertex: float('inf') for vertex in graph}  # Dicionário para armazenar o melhor custo até cada nó
    best_cost[start] = 0  # O melhor custo para o nó inicial é 0
    came_from = {}  # Dicionário para armazenar o caminho de volta para reconstruir o caminho

    while not open_set.empty():
        _, current = open_set.get()  # Obtém o nó com menor custo estimado da fila de prioridade

        # Se o nó atual é o objetivo, reconstrói o caminho e retorna
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return len(path), best_cost[
                goal], path  # Retorna o comprimento do caminho, o custo do caminho e o próprio caminho

        # Explora os vizinhos do nó atual
        for neighbor, cost in graph[current]['edges']:
            total_cost = best_cost[current] + cost
            # Se o custo total até o vizinho for menor que o melhor custo conhecido até o momento
            if total_cost < best_cost[neighbor]:
                best_cost[neighbor] = total_cost  # Atualiza o melhor custo para o vizinho
                open_set.put((total_cost, neighbor))  # Adiciona o vizinho à fila de prioridade
                came_from[neighbor] = current  # Atualiza o nó pai do vizinho

    return 0, float('inf'), []  # Retorna se não encontrou um caminho
