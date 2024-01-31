import math
import datetime

def calculate_tire_volume(width, aspect_ratio, wheel_diameter):
    # Convert wheel diameter from inches to millimeters
    wheel_diameter_mm = wheel_diameter * 25.4
    
    # Calculate the radius of the tire in millimeters
    aspect_ratio_percentage = aspect_ratio / 100.0
    tire_radius = (width * aspect_ratio_percentage + 2 * wheel_diameter_mm) / 2 / 100
    
    # Calculate the volume of the tire in liters
    tire_volume_liters = math.pi * tire_radius**2 * wheel_diameter_mm / 1000

    return tire_volume_liters

def write_to_file(date, width, aspect_ratio, wheel_diameter, tire_volume):
    # Open the file in append mode and write the values to it
    with open('volumes.txt', 'a') as file:
        file.write(f"{date}, {width}, {aspect_ratio}, {wheel_diameter}, {tire_volume:.2f}\n")

def main():
    # Get input from the user
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
    
    # Calculate and display the approximate volume
    tire_volume = calculate_tire_volume(width, aspect_ratio, wheel_diameter)
    
    if tire_volume is not None:
        print(f"The approximate volume is {tire_volume:.2f} liters")
    else:
        print("Error calculating tire volume.")

    # Get the current date
    current_date = datetime.date.today()

    # Write values to the file
    write_to_file(current_date, width, aspect_ratio, wheel_diameter, tire_volume)

    # Additional features to exceed requirements
    # ...

if __name__ == "__main__":
    main()
