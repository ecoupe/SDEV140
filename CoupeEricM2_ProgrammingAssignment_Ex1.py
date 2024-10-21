"""

Author:  Eric Coupe
Date written: 10/21/2024
Assignment:   Module02 Programming Assignment Part 1
Short Desc:   A program that receives input of primary colors. The input
              will be processed and print the result of the mixed colors.
              If a color other than "red" "yellow" or "blue" is input
              the program will show an error.


"""
def primary_color(prompt):
    """
    this function creates a loop to make sure a primary color is input
    """
    while True:
        color = input(prompt)
        if color in ["red", "blue", "yellow"]:
            return color
        else:
            print("Please enter a primary color (red, blue, or yellow).")

def secondary_colors(color1, color2):
    """
    this function combines color options to limit the amount of if 
    statements
    """
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and 
        color2 == "red"):
        return "purple"
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and
        color2 == "red"):
        return "orange"
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and
        color2 == "blue"):
        return "green"

color1 = primary_color("Please enter a primary color: ")
color2 = primary_color("Please enter another primary color: ")
mixing_results = secondary_colors(color1, color2)

print(f"When {color1} and {color2} are combined they make {mixing_results}.")

    

