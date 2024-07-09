from heapq import heappop, heappush
from util import haversine, makeDict2


def a_star(graph, start: int, goal: int) -> tuple:

    grafo_dicionario = makeDict2(graph, goal)
    grafo_dicionario[start]["custo"] = 0
    visitados = set()
    heap = [(0, start)]

    while heap:
        current_node = heappop(heap)[1]
        if current_node in visitados:
            continue
        visitados.add(current_node)
        if current_node == goal:
            break
        for visinho in grafo_dicionario[current_node]["visinhos"]:

            new_cost = (
                grafo_dicionario[current_node]["custo"]
                + grafo_dicionario[current_node]["visinhos"][visinho]
            ) 
            if (
                new_cost < grafo_dicionario[visinho]["custo"]
                and visinho not in visitados
            ): 
                print(visinho)
                grafo_dicionario[visinho][
                    "custo"
                ] = new_cost 
                priority = new_cost + haversine(
                    grafo_dicionario[goal]["posicao"]["x"],
                    grafo_dicionario[goal]["posicao"]["y"],
                    grafo_dicionario[visinho]["posicao"]["x"],
                    grafo_dicionario[visinho]["posicao"]["y"],
                )  
                heappush(heap, (priority, visinho))
                grafo_dicionario[visinho][
                    "anteriores"
                ] = current_node 
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = grafo_dicionario[current_node]["anteriores"]
    path.append(start)
    path.reverse()
    return len(visitados), grafo_dicionario[goal]["custo"], path

