import compute
import network

# Для Барабаши-Альберта
# nw = network.init_network(graph_type='barabasi_albert')

# Для полного графа
nw = network.init_network(graph_type='complete')

theta = 5  # Количество периодов до того, как спин поменяет состояние (можно поменять)