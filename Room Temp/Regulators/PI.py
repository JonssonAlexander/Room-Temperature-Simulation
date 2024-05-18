class PIController:
    """ PI Controller class """
    def __init__(self, kp, ki, setpoint):
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.setpoint = setpoint
        self.integral = 0

    def update(self, current_value):
        """ Calculate the control variable based on PI equations """
        error = self.setpoint - current_value
        self.integral += error

        control_var = self.kp * error + self.ki * self.integral
        return control_var