EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    """
    Calculates the height of the water column between a water tower and tank walls.

    Parameters:
    - tower_height: Height of the water tower in meters.
    - tank_height: Height of the tank walls in meters.

    Returns:
    - Height of the water column in meters.
    """
    return tower_height - tank_height

def pressure_gain_from_water_height(water_height):
    """
    Calculates the pressure gain from the height of the water column.

    Parameters:
    - water_height: Height of the water column in meters.

    Returns:
    - Pressure gain in kilopascals.
    """
    pressure_gain = water_height * WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY / 1000
    return pressure_gain

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    """
    Calculates the water pressure lost due to friction in a pipe.

    Parameters:
    - diameter: Inner diameter of the pipe in meters.
    - length: Length of the pipe in meters.
    - friction_factor: Friction factor (unitless) for the type of pipe.
    - fluid_velocity: Velocity of water flowing through the pipe in meters/second.

    Returns:
    - Lost pressure in kilopascals.
    """
    density_water = WATER_DENSITY
    lost_pressure = (friction_factor * length * density_water * fluid_velocity**2) / (2 * diameter * 1000)
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculates the water pressure lost because of fittings in a pipeline.

    Parameters:
    - fluid_velocity: Velocity of water flowing through the pipe in meters/second.
    - quantity_fittings: Quantity of fittings (e.g., bends) in the pipeline.

    Returns:
    - Lost pressure in kilopascals.
    """
    density_water = WATER_DENSITY
    lost_pressure = -0.04 * density_water * fluid_velocity**2 * quantity_fittings / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates the Reynolds number for a pipe with water flowing through it.

    Parameters:
    - hydraulic_diameter: Hydraulic diameter of the pipe in meters.
                         For a round pipe, it is the same as the inner diameter.
    - fluid_velocity: Velocity of water flowing through the pipe in meters/second.

    Returns:
    - Reynolds number (unitless).
    """
    density_water = WATER_DENSITY
    dynamic_viscosity_water = WATER_DYNAMIC_VISCOSITY
    reynolds_number = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates the water pressure lost due to a pipe diameter reduction.

    Parameters:
    - larger_diameter: Diameter of the larger pipe in meters.
    - fluid_velocity: Velocity of water flowing through the larger diameter pipe in meters/second.
    - reynolds_number: Reynolds number corresponding to the pipe with the larger diameter.
    - smaller_diameter: Diameter of the smaller pipe in meters.

    Returns:
    - Lost pressure in kilopascals.
    """
    density_water = WATER_DENSITY
    k = 0.1 + 50 / (reynolds_number * (larger_diameter / smaller_diameter)**4 - 1)
    lost_pressure = -k * density_water * fluid_velocity**2 / 2000
    return lost_pressure

def kPa_to_psi(kPa_pressure):
    """
    Converts pressure from kilopascals to pounds per square inch (psi).

    Parameters:
    - kPa_pressure: Pressure in kilopascals.

    Returns:
    - Pressure in psi.
    """
    # Conversion factor: 1 kPa = 0.14503773773375 psi
    psi_pressure = kPa_pressure * 0.14503773773375
    return psi_pressure

# Add other functions and constants as needed

def main():
    # Your existing main function code

    # Example: Call the kPa_to_psi function and print the final pressure in both kPa and psi
    final_pressure_kPa = 100.0  # Replace with your calculated final pressure in kPa
    final_pressure_psi = kPa_to_psi(final_pressure_kPa)
    print(f"Final Pressure: {final_pressure_kPa:.2f} kPa / {final_pressure_psi:.2f} psi")

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
