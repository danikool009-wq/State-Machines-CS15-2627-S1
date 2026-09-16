state = "coding"

while True:

    if state == "coding":
        print("You are coding!")

        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "tired":
                state = "sleeping"
                break
            elif feeling == "hungry":
                state = "eating"
                break
            else:
                print("Please enter a valid feeling: tired or hungry.")

    elif state == "eating":
        print("You are eating!")

        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "hungry":
                state = "eating"
                break
            elif feeling == "full":
                state = "coding"
                break
            else:
                print("Please enter a valid feeling: hungry or full.")

    elif state == "sleeping":
        print("You are sleeping!")

        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "hungry":
                state = "eating"
                break
            elif feeling == "awake":
                state = "coding"
                break
            else:
                print("Please enter a valid feeling: hungry or awake.")