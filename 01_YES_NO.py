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

