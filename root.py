


state = "Lab"
while True:

    if state == "Lab":
        print("youre in a Lab")
        event = input("What do you want to view first (Algea/centerfuge machine): ")

        if event == "algea":
            state = "analyze"
        elif event == "centerfuge machine":
            state = "take notes"
        else:
            print("type an actual answer displayed please")

    elif state == "take notes":
        print("youre taking notes of the data for future use!")
        event = input("what should you do next doc? (close eyes/chill): ")

        if event == "close eyes":
            state = "Lab"
        elif event == "chill":
            state = "Leave the lab"
        else:
            print("type an actual answer displayed please")

    elif state == "analyze":
        print("you analyze the experiment before you in awe")
        event = input("What do you want to do? (finish/rest): ")

        if event == "finish":
            state = "leave the lab"
        elif event == "go back to lab":
            state = "Lab"
        else:
            print("type an actual answer displayed please")

    elif state == "leave the lab":
        print("You are outsied the lab and go to get timmies")
        event = input("What do you want to do? (centefuge/go back to lab): ")

        if event == "centerfuge":
            state = "take notes"
        elif event == "go back to lab":
            state = "Lab"
        else:
            print("type an actual answer displayed please")