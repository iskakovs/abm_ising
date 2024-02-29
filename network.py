import random
import networkx as nx

import state

def init_network(graph_type='barabasi_albert'):
    N = state.global_state["N"]
    M = state.global_state["M"]
    
    if graph_type == 'complete':
    G = nx.complete_graph(N)
    else:  # По умолчанию граф Барабаши-Альберта
    G = nx.barabasi_albert_graph(N, M, seed=42)

    nw = {} 
    for node in G.nodes:
        initial_state = random.choice([-1, 1])
        nw[int(node)] = {
            "state": initial_state,
            "new_state": initial_state,
            "neighbors": list(map(lambda x: int(x), G.neighbors(node))),
        }

    del G
    return nw
    
