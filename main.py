import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from algorithms import bfs

# ----------------------
# Build graph from input
# ----------------------
G = nx.Graph()

print("Enter the edges of the graph (Format: A B). Enter a blank line to end input.")

while True:
    line = input()

    if line.strip() == "":
        break

    a, b = line.split()
    G.add_edge(a, b)

start = input("Starting node: ")

# -----------------------------------------------------------------------------
# Spring layout for stable animation, seed = 42 since it is the meaning of life
# -----------------------------------------------------------------------------
pos = nx.spring_layout(G, seed=42)


# Start BFS
plt.ion()

for node, visited in bfs(G, start):
    plt.clf()

    node_colors = [
        "lightgreen" if n in visited else "lightgray"
        for n in G.nodes()
    ]

    # draw graph
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color="red")

    plt.pause(0.8)

plt.ioff()
plt.show()
