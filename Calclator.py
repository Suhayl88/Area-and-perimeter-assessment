import math

def square_choice_checker(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter


def circle_choice_checker_circumference(radius):
    area = math.pi * radius * 2
    circumference = 2 * math.pi * radius
    return area, circumference


def triangle_choice_checker(base_height):
    area = 0.5 * a * b * c
    return area

def rectangle_choice_checker(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

def choice_checker(question, valid_list):
    while True:
        response = input(question)
        for item in valid_list:
            if response == item or response == item[0]:
                return item
        print("Error")

shape_list = ["square", "triangle", "circle", "rectangle"]

# tells the user to pick a shape
shape_choice = choice_checker("Choose a shape : ", shape_list)


def num_check(param):
    pass


# shape calculation
    if shape_choice == "square":
        print("\nit's a square")
        side_length = num_check("\nEnter the side length of your square? ")
        area, perimeter = square_choice_checker(side_length)
        print(f"\nArea of the square =  {area} \n")
        print(f"perimeter of the square = {perimeter}\n")

    elif shape_choice == "circle":
        print("it's a circle")
        radius = num_check("\nEnter the radius of the circle:")
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        print(f"Area of the circle: {area}\n")
        print(f"circumference of the circle {circumference}\n")

    elif shape_choice == "triangle":
        print("Its a triangle")
        a = int(input("Enter the Length of First Side ?: "))
        b = int(input("Enter the Length of Second Side ?: "))
        c = int(input("Enter the Length of Third Side ?: "))
        p = a + b + c
        a = 0.5 * a * b * c
        print("\nPerimeter = ", p)
        print("\nArea = ", a)

    elif shape_choice == "rectangle":
        print("\nit's a rectangle")
        l = num_check("\nEnter the Length of the rectangle ?:")
        b = num_check("\nEnter the base of the rectangle ?: ")
        a = l*b
        p = 2*(l+b)
        print("\nArea = ", a)
        print("\nPerimeter = ", p)
