# main routine goes here
want_instructions = yes_no("\nDo you want to read the instructions?").lower()

if want_instructions == "yes" or want_instructions == "y":

    print("Instructions go here")
    print()

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")
    print("Which shape would you like to choose?")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print()

    print("If you choose square you will receive perimeter and area."
          "\nif you choose circle you will receive the area and the circumference."
          "\nif you choose triangle you will receive the base and length."
          "\nif you choose rectangle you will receive both area and perimeter. ")
    print()