import numpy as np

def brownian_motion(start_position, num_steps, step_size=0.005, lower_bound=0.38, upper_bound=0.42):
    """
    Simulate Brownian motion within a specified range.

    :param start_position: Initial position of the Brownian particle.
    :param num_steps: Number of steps in the simulation.
    :param step_size: Maximum change per step.
    :param lower_bound: Lower bound of the motion.
    :param upper_bound: Upper bound of the motion.
    :return: List of positions during the Brownian motion.
    """
    positions = [start_position]
    current_position = start_position

    for _ in range(num_steps):
        # Random step
        step = np.random.uniform(-step_size, step_size)
        new_position = current_position + step

        # Ensure new position stays within bounds
        new_position = max(min(new_position, upper_bound), lower_bound)
        
        positions.append(new_position)
        current_position = new_position

    return positions