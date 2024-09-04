# functions go here
# import libraries
import math
import pandas



# *** Functions go here ****
# checks that user has answered yes or no

# dictionaries to hold calculation details
problem_shapes = []
problem_dimensions = []
problem_Perimeter = []
problem_Area = []

base_dict = {
    "Shapes": problem_shapes,
    "Dimensions": problem_dimensions,
    "Perimeter": problem_Perimeter,
    "Area": problem_Area
}

def yes_no(question):
    while True:

       # asks question and puts answer into lowercase
        response = input(question).lower()

        # returns 'yes' or 'no' for valid responses
        if response == "y" or response == "yes":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        # if response is invalid, outputs error
        # (and goes to start of loop)
        else:
            print("Please enter yes / no (y / n)")


def choice_checker(question, valid_list):
    while True:
        response = input(question).lower()
        for item in valid_list:
            if response == item or response == item[0]:
                return item
        print("Error")


def not_blank(question, error):
    valid = False
    while not valid:
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
    area = math.pi * radius * 2
    circumference = 2 * math.pi * radius
    return area, circumference


def triangle_choice_checker(base_height):
    s = (a + b + c) / 2

def rectangle_choice_checker(width_length,):
    area = width_length ** 2
    perimeter = a = c = 2 # b = d= 4 #


def num_check(question):
    while True:
        try:

            response = float(input(question))

            if response <= 0:
                print("Error")

            else:
                return response

        except ValueError:
            print("\nWhy you typing nonsense?")


# main routine goes here
want_instructions = yes_no("\nDo you want to read the instructions dear? ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print("If you choose square you will receive perimeter and area."
          "\nif you choose circle you will receive the area and the circumference."
          "\nif you choose triangle you will receive the length of three sides."
          "\nif you choose rectangle you will receive both area and perimeter. ")
    print()
    print("Which shape would you like to choose?")
    print("1. square")
    print("2. circle")
    print("3. triangle")
    print("4. rectangle")
    print()

if want_instructions == "no" or want_instructions == "n":
    print("\nSquare, Circle, Triangle, Rectangle) \n")

while True:
    shape_list = ["square", "triangle", "circle", "rectangle"]

    base_frame = pandas.DataFrame(base_dict)

# tells the user to pick a shape
    shape_choice = choice_checker("\nChoose a shape : ", shape_list)

    # Square Calculation
    if shape_choice == "square":
        print("\nit's a square")
        side_length = num_check("\nEnter the side length of your square? ")
        area, perimeter = square_choice_checker(side_length)
        print(f"\nArea of the square =  {area} \n")
        print(f"perimeter of the square = {perimeter}\n")

# Circle Calculation
    elif shape_choice == "circle":
        print("Its a circle")
        radius = num_check("\nEnter the radius of the circle:")
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"Area of the circle: {area}\n")
        print(f"circumference of the circle {circumference}\n")

# Triangle Calculation
    elif shape_choice == "triangle":
        a = float(input('Enter the length of first side: '))
        b = float(input('Enter the length second side: '))
        c = float(input('Enter the length third side: '))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - c) * (s - b) * (s - a))
        perimeter = a + b + c
        print(f"Area: {area}, Perimeter: {perimeter}")

# Rectangle Calculation
    elif shape_choice == "rectangle":
        print("\nit's a rectangle")
        l = num_check("\nEnter the Length of the rectangle ?:")
        b = num_check("\nEnter the base of the rectangle ?: ")
        a = l*b
        p = 2*(l+b)
        print("\nArea = ", a)
        print("\nPerimeter = ", p)

# ask user if they want to end program
    keep_going = input("\nPress enter to end or anything else to continue...")
    print()

    # if the user presses <enter> end the loop
    if keep_going == "":
        print("we are done thank you soo much."
              "!")
        break

    print()


# add shape name
problem_shapes.append(problem_shapes)
problem_dimensions.append(problem_dimensions)
problem_Perimeter.append(problem_Perimeter)
problem_Area.append(problem_Area)

# create data frame from dictionary to organise information
base_frame = pandas.DataFrame(base_dict)

# output table within Shape data
print(base_frame)













