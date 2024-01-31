import math

def main():
    print("This program computes the volume of a right circular cone.")
    print("For example, if the radius of a cone is 2.8 and")
    print("the height is 3.2, then the volume is 26.3\n")
    
    # Get user input for radius and height
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))
    
    # Call cone_volume function and display the results
    cone_volume(radius, height)


def cone_volume(radius, height):
    """Compute and print the volume of a right circular cone.

    Parameters
        radius: The radius of the cone.
        height: The height of the cone.
    """
    # Formula for the volume of a cone
    volume = (1/3) * math.pi * radius**2 * height
    
    # Display the results
    print("\nRadius:", radius)
    print("Height:", height)
    print("Volume:", round(volume, 1))


# Call the main function
main()
