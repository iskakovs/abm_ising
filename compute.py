import numpy as np

import state

def compute_iter(nw, current_iter, theta):
    for key, value in nw.items():
        eps_minus, eps_plus = _generate_epsilon()
        neighbor_thoughts = [nw[n]["state"] for n in value["neighbors"]]

        u_minus, u_plus = _generate_utility(neighbor_thoughts, eps_minus, eps_plus)

        selected_state = 1 if u_plus > u_minus else -1
        # Сохраняем выбранное состояние и итерацию, когда был сделан выбор
        nw[key]["selected_state"] = selected_state
        nw[key]["selected_iter"] = current_iter
