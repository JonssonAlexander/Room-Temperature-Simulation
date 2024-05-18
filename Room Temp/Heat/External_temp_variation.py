import numpy as np
def external_temperature_variation(day, min_temp=4, max_temp=17):
    """
    Ändrar på yttertemp 
    """
    daily_variation = (np.sin(2 * np.pi * day / 30) + 1) *0.5   # Normalized between 0 and 1
    return min_temp + (max_temp - min_temp) * daily_variation