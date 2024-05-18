def apply_window_effect(room, window_locations, external_temp, window_effect_strength=0.1):
    """
    Apply the effect of windows on the room's temperature.

    :param room: The numpy array representing room temperature.
    :param window_locations: A list of tuples representing window locations.
    :param external_temp: The current external temperature.
    :param window_effect_strength: The strength of the external temperature's effect through the window.
    :return: Updated room temperature.
    """
    for window_location in window_locations:
        win_x, win_y = window_location
        
        # Directly adjust the temperature at the window location
        room[win_x, win_y] = (1 - window_effect_strength) * room[win_x, win_y] + window_effect_strength * external_temp
        # You can expand this to affect nearby tiles if needed
    return room