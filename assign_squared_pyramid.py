#!/usr/bin/env python3\
# Created By:Kamche
# Created on: September 24, 2026
# This program ask the user for the side length
# and the height of a squared pyramid in mm.
# It then calculates and displays the volume of the squared pyramid
import math

import constants


def main():
    # Welcome message
    print("Welcome to Kamche Pyramid Calculator!")
    name = input("Please enter your name to start the program: ")
    print(f"Hello, {name}!")

    # Ask the user for the side length and height of the squared pyramid
    side_length = int(input("Enter the side length of the squared pyramid in mm: "))
    height = int(input("Enter the height of the squared pyramid in mm: "))

    # Convert the side length and height to an integer
    side_length = int(side_length)
    height = int(height)

    # Calculate the surface area of the squared pyramid
    surface_area = (side_length**2) + (
        2 * side_length * math.sqrt(height**2 + (side_length / 2) ** 2)
    )

    # Calculate the volume of the squared pyramid
    volume = constants.VOLUME_CONSTANT * (side_length**2) * height

    # Display the surface area and volume of the squared pyramid
    print(
        f"The surface area of the squared pyramid is {surface_area:.{constants.DECIMAL_PLACES}f} mm²."
    )
    print(
        f"The volume of the squared pyramid is {volume:.{constants.DECIMAL_PLACES}f} mm³."
    )


if __name__ == "__main__":
    main()
