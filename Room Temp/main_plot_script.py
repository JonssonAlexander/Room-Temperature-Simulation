import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import TwoSlopeNorm

from Heat.External_temp_variation import external_temperature_variation
from Heat.Apply_Realistic_Fan_Heat import apply_realistic_fan_heat
from Heat.Heat_Diffusing import diffuse_heat_with_ext_temp_corrected

from Windows.Window_Cooling import apply_window_effect
from Windows.Current import diffuse_heat_with_air_currents
from Windows.Current import calculate_air_currents

from Regulators.FeedForward import feedforward_control
from Regulators.PI import PIController

from Brownian_Motion.Brownian_motion import brownian_motion


"""
Ändra brownian motion om den ballar ur i filen Brownian_motion.py
"""
start_position = 0.4  # Starting in the middle of the range
num_steps = 1000  # Number of steps in the Brownian motion
D = brownian_motion(start_position, num_steps)


initial_temp = 13.57
desired_room_temp = 28

room_size = (15, 15)
room = np.full(room_size, initial_temp)

feedforward_gain = 0.3
pi = PIController(kp=0.1, ki=0.05, setpoint=desired_room_temp)

"""
Vilka delar av rummet vi vill undersöka!
"""
center_tile = (7, 7)
corner_tile = (0, 0)
edge_tile = (0, 7)

# Lists to track the temperatures
center_tile_temp = []
corner_tile_temp = []
edge_tile_temp = []
external_temps = []

"""
Change fan locations: 
"""
fan_locations = [(0, 0), (0, 15), (15, 0), (15, 15)]
window_locations = [(5, 0), (6, 0), (7, 0), (8, 0), (14, 2), (14, 3), (14, 4)] 

fan_power_list = []
pi_control_list = []
for day in range(1000):  # Simulating for 1000 days
    ext_temp = external_temperature_variation(day % 30)  # External temperature
    mean_room = np.mean(room)
    
    ff_control = feedforward_control(ext_temp, desired_room_temp, feedforward_gain)
    
    pi_control = pi.update(mean_room)
    pi_control_list.append(pi_control)
    fan_power = pi_control + ff_control
    fan_power_list.append(fan_power)
    fan_power = max(0, min(fan_power, 2))
    print(fan_power)
    air_currents = calculate_air_currents(room, fan_locations, fan_power)

    room = diffuse_heat_with_air_currents(room, air_currents, D[day])
    room = apply_realistic_fan_heat(room, fan_power)
    room = apply_window_effect(room, window_locations, ext_temp)
    room = diffuse_heat_with_ext_temp_corrected(room, ext_temp)
    #room = np.clip(room, a_min=None, a_max=31)  # Ensure max temperature is not exceeded

    # Track temperatures
    center_tile_temp.append(room[center_tile])
    corner_tile_temp.append(room[corner_tile])
    edge_tile_temp.append(room[edge_tile])
    external_temps.append(ext_temp)

print('Pi-Fan',np.array(pi_control_list)-np.array(fan_power_list))


plt.figure(figsize=(10, 6))
plt.plot(center_tile_temp[10:], label="Center Tile")
plt.plot(corner_tile_temp[10:], label="Corner Tile")
plt.plot(edge_tile_temp[10:], label="Edge Tile")
plt.plot(external_temps[10:], label="External Temperature", linestyle='--')
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Tracking with External Influence")
plt.legend()
plt.show()
"""
plt.plot(D)
plt.title('Brownian motion for Diffuse constant D')
plt.show()
"""