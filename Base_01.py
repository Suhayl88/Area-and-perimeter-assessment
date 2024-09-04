# functions go here
# import libraries
# import pandas

# *** Functions go here ****
# checks that user has answered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y" or response == "ye":
            return "yes"

        elif response == "no" or response == "n" or response == "nope":
            return "no"

        else:
            print("Please enter yes or no")


# main routine goes here
want_instructions = yes_no("\nDo you want to read the instructions?").lower()

if want_instructions == "yes" or want_instructions == "y":

    print("Instructions go here")
    print()

    print("Please select (Circle, Square, Triangle, Rectangle or 'xxx' to quit) ")
    print()




