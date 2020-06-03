#Find Minimal path from graph using kruskal algorithm

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([
        ('a', 'b', {'weight':2, 'label': 2}), 
        ('a', 'c', {'weight':3, 'label': 3}), 
        ('a', 'd', {'weight':1, 'label': 1}), 
        ('a', 'e', {'weight':3, 'label': 3}), 
        ('b', 'c', {'weight':4, 'label': 4}), 
        ('c', 'd', {'weight':5, 'label': 5}), 
        ('d', 'e', {'weight':4, 'label': 4}), 
        ('e', 'a', {'weight':1, 'label': 1})
    ])
draw(G, layout='circo')

T = nx.minimum_spanning_tree(G)
for e in T.edges():
    G[e[0]][e[1]]['color'] = 'blue'
draw(G, layout='circo')