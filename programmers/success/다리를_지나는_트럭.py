# 2026-09-15
from collections import deque


def solution(bridge_length, weight, truck_weights):
    wait_trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    time = 0

    while wait_trucks:
        time += 1
        exited = bridge.popleft()
        current_weight -= exited
        if current_weight + wait_trucks[0] <= weight:
            entering_truck = wait_trucks.popleft()
            bridge.append(entering_truck)
            current_weight += entering_truck
        else:
            bridge.append(0)

    return time + bridge_length
