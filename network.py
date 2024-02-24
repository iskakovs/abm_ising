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
