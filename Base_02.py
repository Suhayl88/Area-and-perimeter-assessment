# Import libraries
import math
import pandas as pd


# *** Functions go here ****
# Checks that user has answered yes or no
def yes_no(question):
    while True:
        # Asks question and puts answer into lowercase
        response = input(question).lower()
        # Returns 'yes' or 'no' for valid responses
        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            # If response is invalid, outputs error
            print("Please enter yes / no (y / n)")


def choice_checker(question, valid_list):
    while True:
        response = input(question).lower()
        for item in valid_list:
            if response == item or response == item[0]:
                return item
        print("Error why you typing nonsense.")


def not_blank(question, error):
    while True:
        response = input(question)
        if response == "":
            print(f"{error}. \nPlease try again.\n")
            continue
        return response


def square_choice_checker(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter


def circle_choice_checker(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


def triangle_choice_checker(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return area, perimeter


def rectangle_choice_checker(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


def num_check(question):
    while True:
        try:
            response = float(input(question))
            if response <= 0:
                print("Error: The value must be greater than zero.")
            else:
                return response
        except ValueError:
            print("\nError: Please enter a valid number.")


# Dictionaries to hold calculation details
problem_shapes = []
problem_dimensions = []
problem_perimeter = []
problem_area = []
base_dict = {
    "Shapes": problem_shapes,
    "Dimensions": problem_dimensions,
    "Perimeter": problem_perimeter,
    "Area": problem_area
}

# Main routine goes here
want_instructions = yes_no("\nDo you want to read the instructions? ").lower()
if want_instructions == "yes":
    print("If you choose square, you will receive perimeter and area."
          "\nIf you choose circle, you will receive the area and the circumference."
          "\nIf you choose triangle, we assume you have 3 sides."
          "\nIf you choose rectangle, you will receive both area and perimeter.")
    print()
    print(" Which Shape would you like to choose")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print()

if want_instructions == "no" or want_instructions == "n":
    print()
    print(" Which Shape would you like to choose")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print()

shape_list = ["square", "circle", "triangle", "rectangle"]

while True:
    # Create DataFrame to store calculation results
    base_frame = pd.DataFrame(base_dict)

    # Tells the user to pick a shape
    shape_choice = choice_checker("\nChoose a shape: ", shape_list)

    # Square Calculation
    if shape_choice == "square":
        print("\nIt's a square")
        side_length = num_check("\nEnter the side length of your square? ")
        area, perimeter = square_choice_checker(side_length)
        print(f"\nArea of the square = {area} \n")
        print(f"perimeter of the square = {perimeter}\n")
        dimension = f"Side: {side_length}"

    # Circle Calculation
    elif shape_choice == "circle":
        print("It's a circle")
        radius = num_check("\nEnter the radius of the circle: ")
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"Area of the circle: {area}\n")
        print(f"circumference of the circle {circumference}\n")
        dimension = f"Radius: {radius}"

    # Triangle Calculation
    elif shape_choice == "triangle":
        print("It's a triangle")
        a = num_check('Enter the length of the first side: ')
        b = num_check('Enter the length of the second side: ')
        c = num_check('Enter the length of the third side: ')
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - c) * (s - b) * (s - a))
        perimeter = a + b + c
        print(f"Area: {area}, Perimeter: {perimeter}")
        dimension = f"Sides: {a}, {b}, {c}"

    # Rectangle Calculation
    elif shape_choice == "rectangle":
        print("\nIt's a rectangle")
        length = num_check("\nEnter the length of the rectangle: ")
        width = num_check("\nEnter the width of the rectangle: ")
        area = length * width
        perimeter = 2 * (length + width)
        print("\nArea = ", area)
        print("\nPerimeter = ", perimeter)
        dimension = f"Length: {length}, Width: {width}"

    # table calculation
    problem_shapes.append(shape_choice)
    problem_dimensions.append(dimension)
    problem_area.append(area)
    problem_perimeter.append(perimeter)

    # Ask user if they want to continue or end the program
    keep_going = input("\nPress Enter to end or type anything else to continue... ")
    if keep_going == "":
        print("We are done. Thank you so much!")
        break

# Create DataFrame
base_frame = pd.DataFrame(base_dict)

# print the table
print(base_frame)
