def feedforward_control(external_temp, desired_room_temp, feedforward_gain):
    """
    Calculate the feedforward control action based on external temperature.

    :param external_temp: The external temperature.
    :param desired_room_temp: The desired room temperature.
    :param feedforward_gain: The gain factor for feedforward control.
    :return: The feedforward control action.
    """
    control_action = feedforward_gain * (desired_room_temp - external_temp)
    return control_action