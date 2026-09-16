state = "class"

while True:

    if state == "class":
        print("You are in class!")
        event = input("What do you want to do? (study/break): ").lower()

        if event == "study":
            state = "homework"
        elif event == "break":
            state = "lunch"
        else:
            print("Invalid event. Your state has not changed.")

    elif state == "lunch":
        print("You are eating lunch!")
        event = input("What do you want to do? (eat/play): ").lower()

        if event == "eat":
            state = "class"
        elif event == "play":
            state = "recreation"
        else:
            print("Invalid event. Your state has not changed.")

    elif state == "homework":
        print("You are doing homework!")
        event = input("What do you want to do? (finish/rest): ").lower()

        if event == "finish":
            state = "recreation"
        elif event == "rest":
            state = "class"
        else:
            print("Invalid event. Your state has not changed.")

    elif state == "recreation":
        print("You are relaxing!")
        event = input("What do you want to do? (study/sleep): ").lower()

        if event == "study":
            state = "homework"
        elif event == "sleep":
            state = "class"
        else:
            print("Invalid event. Your state has not changed.")