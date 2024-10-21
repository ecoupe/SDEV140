"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module01 Practice Exercise 2-2
Short Desc:   A program that calculates the surface area of a cube.
              User will input the length of an edge of the cube.


"""

cube_edge = float(input("Enter the edge length: "))
surface_area = 6*pow(cube_edge,2)

print(f"The surface area of this square is: {surface_area:,.2f}")
