"""Implementação de uma estrutura de grafo."""

import sys


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    graph = {}
    with open(filename, "rt") as input_file:
        vertex_count = int(input_file.readline().strip())  # File needs to start with coords quantity number

        for i in range(vertex_count):  # Counts every coord
            index, latitude, longitude = input_file.readline().strip().split()

            graph[int(index)] = {'vertex': (float(latitude), float(longitude)), 'edges': []}

        edge_count = int(input_file.readline().strip())  # File needs to have possibility quantity number after coords

        for j in range(edge_count):  # Counts every possibility
            from_vertex, to_vertex, cost = (
                input_file.readline().strip().split()
            )

            from_vertex, to_vertex, cost = int(from_vertex), int(to_vertex), float(cost)
            graph[from_vertex]['edges'].append((to_vertex, cost))

    return graph

# graph = {
#     0: {'coord': (-30.008646, -51.142909), 'edges': [(2, 93.16199226823055), (9, 370.84011298540076)]},
#     1: {'coord': (-30.00894, -51.143344), 'edges': [(2, 40.19992641024175), (0, 53.13321306005169)]},
#     2: {'coord': (-30.009126, -51.143702), 'edges': [(5, 128.56119211286216), (9, 278.0130930702961)]},
#     3: {'coord': (-30.009509, -51.14423), 'edges': [(1, 106.2128991394714), (2, 66.32082803669168), (4, 44.93938270233482), (5, 62.612803936405655)]},
#     4: {'coord': (-30.009731, -51.14462), 'edges': [(2, 17.77830304610445), (5, 81.63281218293855), (7, 137.6521663708679)]},
#     5: {'coord': (-30.009801, -51.144786), 'edges': [(2, 128.56119211286216), (4, 17.77830304610445), (6, 81.63281218293855), (7, 119.89850426306808), (9, 150.92654043736871)]},
#     6: {'coord': (-30.01014, -51.145538), 'edges': [(5, 81.63281218293855), (7, 38.37761880079564), (8, 57.258847924240776), (9, 69.64300121602454)]},
#     7: {'coord': (-30.010327, -51.145873), 'edges': [(4, 137.6521663708679), (5, 119.89850426306808), (6, 38.37761880079564), (8, 20.481000375464983)]},
#     8: {'coord': (-30.010342, -51.146085), 'edges': [(7, 20.481000375464983), (9, 12.941289400664326)]},
#     9: {'coord': (-30.010351, -51.146219), 'edges': [(0, 370.84011298540076), (2, 278.0130930702961), (5, 150.92654043736871), (6, 69.64300121602454), (8, 12.941289400664326)]}
# }

