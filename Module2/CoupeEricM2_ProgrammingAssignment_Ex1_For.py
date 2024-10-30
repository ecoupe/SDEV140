"""

Author:  Eric Coupe
Date written: 10/30/2024
Assignment:   Module02 Programming Assignment Part 1
Short Desc:   A program that receives input of primary colors. The input
              will be processed and print the result of the mixed colors.
              If a color other than "red" "yellow" or "blue" is input
              the program will show an error. Trying the code with a
              For loop instead of While loops.


"""
# this sets an array to compare input to
primary_colors = ["red", "blue", "yellow"]

# creates an open array to store input
colors = []
for i in range(2):
    valid_input = False #using this as a gate for the loop
    #limits attempts to ensure valid input
    for attempt in range(5):
        # here we ask for input of color 1 and 2 
        color = input(f"Please enter primary color {i+1}: ")
        if color in primary_colors:
            colors.append(color)
            valid_input = True
            break
        else:
            print("Please enter a primary color (red, blue, or yellow).")
    if not valid_input:
        print("Too many invalid attempts, exiting.")
        exit()

# setting both variables = to the array. color1 will take first input
# color 2 will take second input
color1, color2 = colors

mixing_results = ""
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and 
    color2 == "red"):
    mixing_results = "purple"
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" 
      and color2 == "red"):
    mixing_results = "orange"
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" 
      and color2 == "blue"):
    mixing_results = "green"

print(f"When {color1} and {color2} are combined they make" \
          f" {mixing_results}")