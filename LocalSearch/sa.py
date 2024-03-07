import math
import random

def objective_function(x):
    return -((x - 5) ** 2)

def get_neighbour(current, max_step):
    print("Max Step Random: ", random.uniform(-max_step, max_step))
    return current + random.uniform(-max_step, max_step)

def accept_probability(delta_e, temperature):
    if delta_e > 0:
        return math.exp(-delta_e / temperature)
    else:
        return 1.0


def simulated_annealing_search(initial_state, max_iterations, max_step, initial_temperature, cooling_rate):
    current_state = initial_state
    current_value = objective_function(initial_state)
    best_state = current_state
    best_value = current_value
    temperature = initial_temperature

    for i in range(max_iterations):
        print(i)
        neighbour_state = get_neighbour(current_state, max_step)
        neighbour_value = objective_function(neighbour_state)
        delta_e = neighbour_value - current_value
        print("Neightbor State: ", neighbour_state)
        print("Neightbor Value: ", neighbour_value)
        print("DeltaE: ", delta_e)

        if delta_e < 0 or random.random() < accept_probability(delta_e, temperature):
            print("Random: ", random.random())
            current_state = neighbour_state
            current_value = neighbour_value
            print("Current State: ", current_state)
            print("Current Value: ", current_value)

        if current_value < best_value:
            best_state = current_state
            best_value = current_value
            print("Best State: ", best_state)
            print("Best Value: ", best_value)

        temperature *= cooling_rate
        print("Temperature: ", temperature, "\n--------------------\n")

    return best_state, best_value

initial_state = 0  # ตำแหน่งเริ่มต้น
max_iterations = 500  # จำนวนการทำซ้ำสูงสุด
max_step = 0.1  # ขนาดของการเคลื่อนไหวสูงสุดในแต่ละขั้น
initial_temperature = 1000  # อุณหภูมิเริ่มต้น
cooling_rate = 0.95  # อัตราการลดอุณหภูมิ

best_state, best_value = simulated_annealing_search(
    initial_state, max_iterations, max_step, initial_temperature, cooling_rate)
print("Best State:", best_state)
print("Best Value:", best_value)
