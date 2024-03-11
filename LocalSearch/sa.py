import math
import random


def objective_function(x):
    return -((x - 5) ** 2) # -((0.0810 - 5) ^ 2) = -24.1966

#                    0        0.1
def get_neighbour(current, max_step):
    print("Max Step Random: ", random.uniform(-max_step, max_step))
    print("Get Neighbor: ", current + random.uniform(-max_step, max_step))
    return current + random.uniform(-max_step, max_step) # 0 + random(-0.1, 0.1) = 0.0914


def accept_probability(delta_e, temperature): # -0.1023, 950
    if delta_e > 0:
        return math.exp(-delta_e / temperature) # 2.71828 ^ -0.9057/1000 = 0.9999
    else:
        return 1.0

#                                   0              500          0.1            1000                0.95
def simulated_annealing_search(initial_state, max_iterations, max_step, initial_temperature, cooling_rate):
    current_state = initial_state # cs = 0.0914
    current_value = objective_function(initial_state) # cv = -24.0943
    best_state = current_state # bs = 0
    best_value = current_value # bv = -25
    temperature = initial_temperature # tmp = 902.5

    for i in range(max_iterations):
        print(i) # i = 1
        neighbour_state = get_neighbour(current_state, max_step) # ns = 0.0810
        neighbour_value = objective_function(neighbour_state) # nv = -24.1966
        delta_e = neighbour_value - current_value # de = -0.1023
        print("Neightbor State: ", neighbour_state)
        print("Neightbor Value: ", neighbour_value)
        print("DeltaE: ", delta_e)
    #      -0.1023 > 0? or     0.2829     <          1.0
        if delta_e > 0 or random.random() < accept_probability(delta_e, temperature):
            print("Random: ", random.random())
            current_state = neighbour_state # cs = 0.0810 
            current_value = neighbour_value # cv = -24.1966
            print("Current State: ", current_state)
            print("Current Value: ", current_value)
        #     -24.1966   >  -24.0943
        if current_value > best_value:
            best_state = current_state # bs = 0.0914
            best_value = current_value # bv = -24.0943
            print("Best State: ", best_state)
            print("Best Value: ", best_value)

        temperature *= cooling_rate # tmp = 902.5
        print("Temperature: ", temperature, "\n--------------------\n")

    return best_state, best_value


initial_state = 0  # ตำแหน่งเริ่มต้น
max_iterations = 50000  # จำนวนการทำซ้ำสูงสุด
max_step = 0.1  # ขนาดของการเคลื่อนไหวสูงสุดในแต่ละขั้น
initial_temperature = 1000  # อุณหภูมิเริ่มต้น
cooling_rate = 0.95  # อัตราการลดอุณหภูมิ

best_state, best_value = simulated_annealing_search(initial_state, max_iterations, max_step, initial_temperature, cooling_rate)
print("Best State:", best_state)
print("Best Value:", best_value)
