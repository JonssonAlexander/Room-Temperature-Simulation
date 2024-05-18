#import numpy as np
def apply_realistic_fan_heat(room, fan_power, max_distance=3):
    for i in range(room.shape[0]):
        for j in range(room.shape[1]):
            distance_from_edge = min(i, j, room.shape[0] - i - 1, room.shape[1] - j - 1)
            if distance_from_edge < max_distance:
                heat = fan_power * (1 - distance_from_edge / max_distance)
                room[i, j] += heat
    return room