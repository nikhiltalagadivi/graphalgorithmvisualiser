import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# make the graph
G = nx.Graph()

print("Enter the edges of the graph (Format: A B). Enter a blank line to end input.")

while True:
    line = input()

    if line.strip() == "":
        break

    a, b = line.split()
    G.add_edge(a, b)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color="lightblue")

plt.show()
