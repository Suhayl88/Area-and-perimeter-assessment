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

