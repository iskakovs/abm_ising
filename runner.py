import compute
import network

# Для Барабаши-Альберта
# nw = network.init_network(graph_type='barabasi_albert')

# Для полного графа
nw = network.init_network(graph_type='complete')

theta = 5  # Количество периодов до того, как спин поменяет состояние (можно поменять)

for i in range(500):
    compute.compute_iter(nw, current_iter=i, theta=theta)
    compute.finish_iter(nw, current_iter=i, theta=theta)

    plus_state = len([x for x in nw.values() if x["state"] == 1])
    print(f'Iter: {i + 1}, plus_state: {plus_state/len(nw)}')
