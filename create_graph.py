# import matplotlib.pyplot as plt
import networkx as nx
import community

from networkx.algorithms.approximation.clique import max_clique
from networkx.readwrite import json_graph

with open("edges.csv", "rb") as f:
    header = f.readline()
    G = nx.read_edgelist(f, delimiter=',', nodetype=int)

try:

    from colors import colors, hex_to_rgb, rgbs

    #Run community detection algorithm
    print('Detecting communities...')
    myCNM = community.CNM(G)
    comms = myCNM[1]

    #Calculate node positions
    print('Laying out nodes...')
    pos = nx.spring_layout(G, iterations = 1000, scale = 1000)

    print('Saving attributes...')
    #Add the visual attrs to each node
    for i in range(len(comms)):
        for n in comms[i]:
            G.node[n]['viz']={'color': rgbs[i], 'position':{'x':pos[n][0], 'y':pos[n][1]}}

    #Export to 'venmo.gexf'
    nx.write_gexf(G, 'venmo.gexf')

except Exception as e:
    print(e)
    import pdb; pdb.set_trace()
    print('hello')
