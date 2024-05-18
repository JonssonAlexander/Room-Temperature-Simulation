def diffuse_heat_with_ext_temp_corrected(room, ext_temp):
    new_room = room.copy()
    """
    Airflow: Ändras efter verkliga förhållanden! 
    """
    airflow_factor = 0.3  # Represents the effect of airflow in equalizing the room temperature

    for i in range(room.shape[0]):
        for j in range(room.shape[1]):
            # Collect neighbor temperatures, including external temperature for edge cells
            neighbor_temps = []
            if i > 0:
                neighbor_temps.append(room[i-1, j])
            else:
                neighbor_temps.append(ext_temp)

            if i < room.shape[0] - 1:
                neighbor_temps.append(room[i+1, j])
            else:
                neighbor_temps.append(ext_temp)

            if j > 0:
                neighbor_temps.append(room[i, j-1])
            else:
                neighbor_temps.append(ext_temp)

            if j < room.shape[1] - 1:
                neighbor_temps.append(room[i, j+1])
            else:
                neighbor_temps.append(ext_temp)

            avg_neighbor_temp = sum(neighbor_temps) / len(neighbor_temps)
            new_room[i, j] = (1 - airflow_factor) * room[i, j] + airflow_factor * avg_neighbor_temp

    return new_room