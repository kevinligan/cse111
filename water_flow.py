def water_column_height(tower_height, tank_height):
    """
    Calculates and returns the height of a column of water from a tower height and a tank wall height.

    Parameters:
        tower_height (float): Height of the tower.
        tank_height (float): Height of the walls of the tank on top of the tower.

    Returns:
        float: Height of the water column.
    """
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """
    Calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.

    Parameters:
        height (float): Height of the water column.

    Returns:
        float: Pressure in kilopascals.
    """
    density_water = 998.2  # kilogram / meter^3
    gravity_acceleration = 9.80665  # meter / second^2
    return density_water * gravity_acceleration * height / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe.

    Parameters:
        pipe_diameter (float): Diameter of the pipe in meters.
        pipe_length (float): Length of the pipe in meters.
        friction_factor (float): Pipe’s friction factor.
        fluid_velocity (float): Velocity of the water flowing through the pipe in meters / second.

    Returns:
        float: Lost pressure in kilopascals.
    """
    density_water = 998.2  # kilogram / meter^3
    return -friction_factor * pipe_length * density_water * fluid_velocity**2 / (2000 * pipe_diameter)
