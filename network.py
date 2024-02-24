import random
import networkx as nx

import state

def init_network(graph_type='barabasi_albert'):
    N = state.global_state["N"]
    M = state.global_state["M"]
