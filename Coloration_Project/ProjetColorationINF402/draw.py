import matplotlib.pyplot as plt
import networkx as nx
from graphes import listedegraphes
from main import creer_Dimac_fich,interprete_solution,solve_sat_from_dimacs_file
graphe = listedegraphes['graphe2']
couleurs=[1,2,3,4,5,6]


def draw_graph(graph):
    G = nx.Graph()

    # Ajouter les sommets au graphe
    G.add_nodes_from(range(1, len(graph['graphe'])+1 ))

    # Ajouter les arêtes au graphe
    for vertex, neighbors in enumerate(graph['graphe'], start=1):
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor)

    # Disposition automatique des sommets
    pos = nx.spring_layout(G)

    # Dessiner le graphe
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold', edge_color='black', linewidths=1, arrows=False)

    plt.title("Représentation du graphe")
    plt.show()


def draw_colored_graph(graph, colors):
    G = nx.Graph()

    # Ajouter les sommets au graphe
    G.add_nodes_from(range(1, len(graph['graphe'])+1 ))

    # Ajouter les arêtes au graphe
    for vertex, neighbors in enumerate(graph['graphe'], start=1):
        for neighbor in neighbors:
            G.add_edge(vertex, neighbor)

    # Disposition automatique des sommets
    pos = nx.spring_layout(G)

    # Dessiner le graphe avec les couleurs spécifiées
    nx.draw(G, pos, with_labels=True, node_color=[colors[i] for i in range(1, len(graph['graphe'])+1)], node_size=1500, font_size=10, font_weight='bold', edge_color='black', linewidths=1, arrows=False)

    plt.title("Représentation du graphe avec coloration")
    plt.show()
#creer_Dimac_fich(graphe, couleurs, 'inst.dimacs')
#solution_sat,boole=solve_sat_from_dimacs_file("inst.dimacs")
#colors_graph = interprete_solution(solution_sat, len(couleurs))
#draw_colored_graph(graphe,colors_graph)