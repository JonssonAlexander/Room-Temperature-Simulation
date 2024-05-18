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
from Windows.Current import diffuse_heat

from Regulators.FeedForward import feedforward_control
from Regulators.PI import PIController

from Brownian_Motion.Brownian_motion import brownian_motion

start_position = 0.4  # Starting in the middle of the range
num_steps = 1000  # Number of steps in the Brownian motion
D = brownian_motion(start_position, num_steps)


initial_temp = 13.57
desired_room_temp = 29

room_size = (15, 15)
room = np.full(room_size, initial_temp)

feedforward_gain = 0.4
pi = PIController(kp=0.2, ki=0.01, setpoint=desired_room_temp)

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


fig, ax = plt.subplots(figsize=(8, 6))
norm = TwoSlopeNorm(vmin=0, vcenter=22, vmax=31)

"""
Change fan locations: 
"""
fan_locations = [(0, 0), (0, 15), (15, 0), (15, 15)]
window_locations = [(5, 0), (6, 0), (7, 0), (8, 0), (14, 2), (14, 3), (14, 4)] 

def update(frame):
    global room
   
    day = frame % 30  # Simulate a day in April
    ext_temp = external_temperature_variation(day)
    """
    Nedan är antagande kring hur mycket yttertemp påverkar innertemp
    """
    #room = room * 0.90 + ext_temp * 0.1  # Slow adjustment to external temperature

    average_room_temp = np.mean(room)
  
    ff_control = feedforward_control(ext_temp, desired_room_temp, feedforward_gain)
    pi_control = pi.update(average_room_temp)

    fan_power = pi_control + ff_control
    fan_power = max(0, min(fan_power, 1))  # Ensure fan power is within [0, 1]

    air_currents = calculate_air_currents(room, fan_locations, fan_power)

    room = diffuse_heat_with_air_currents(room, air_currents,D[frame])
    room = apply_realistic_fan_heat(room, fan_power)
    room = apply_window_effect(room, window_locations, ext_temp)
    #room = diffuse_heat(room)
    room = diffuse_heat_with_ext_temp_corrected(room, ext_temp)
    room = np.clip(room, a_min=None, a_max=31)  # Ensure max temperature is not exceeded
    
    # Track temperatures
    center_tile_temp.append(room[center_tile])
    corner_tile_temp.append(room[corner_tile])
    edge_tile_temp.append(room[edge_tile])
    external_temps.append(ext_temp)
    
    ax.clear()
    im = ax.imshow(room, cmap='coolwarm', norm=norm)
    #fig.colorbar(im, orientation='vertical',label='Temperature °C')
    ax.set_title(f"Room Temperature")
    print(room)
    ax.axis('off')
    return [im]


ani = animation.FuncAnimation(fig, update, frames=600, blit=True, interval=1, repeat=False)

plt.show()
