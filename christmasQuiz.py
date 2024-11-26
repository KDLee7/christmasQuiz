def christmasQuiz():
    print("Welcome to the Chistmas Quiz!")
    start_game = input("Do you want to play? ").strip().lower()

    if start_game != "yes":
        print("Maybe next time! Have a Merry Christmas!")
        return

    print("Great! Let's start the quiz!")

    score = 0
    #Q & A
    question = input("What is the name of the reindeer with the shiny red nose? ").strip().lower()
    if question == "rudolf":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Rudolf.")

    question = input("In the song The Twleve DAys of Chrismtas, what gift is given on the fifth day? ").strip().lower()
    if question == "5 golden rings":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was 5 Golden Rings.")

    question = input("What is the name of the Grinch's dog in How the Grinch Stole Christmas? ").strip().lower()
    if question == "max":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Max.")

    question = input("Which country is credited with starting the tradition of putting up a Christmas tree? ").strip().lower()
    if question == "germany":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Germany.")

    question = input("In the the movie Home Alone, where is the McCallister family going when they leave Kevin behind? ").strip().lower()
    if question == "paris":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Paris.")

    question = input("What popular Christmas beverage is also called milk punch? ").strip().lower()
    if question == "eggnog":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Eggnog.")

    question = input("Waht are you supposed to do under the mistletoe? ").strip().lower()
    if question == "kiss":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Kiss.")

    question = input("What is the best-selling Christmas song of all time? ").strip().lower()
    if question == "white christmas":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was White Christmas. This was sung by Bing Crosby.")

    question = input("In which modern-day country was Saint Nicholas born? ").strip().lower()
    if question == "turkey":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Turkey.")

    question = input("What were Frost the Snowman's last words? ").strip().lower()
    if question == "i'll be back again someday":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was I'll be back again someday.")

    question = input("What is the highest grossing Christmas movie of all time? ").strip().lower()
    if question == "home alone":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Home Alone.")

    question = input("In Charles Dickens' A Christmas Carol, what is the first name of Scrooge? ").strip().lower()
    if question == "ebenezer":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Ebenezer.")

    question = input("What is the name of the character who helped Rudolf guide Santa's sleigh? ").strip().lower()
    if question == "clarice":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Clarice.")

    question = input("Which country gifts the Christmas tree in Trafalgar Square in London every year? ").strip().lower()
    if question == "norway":
        print("You are correct!")
        score += 1
    else:
        print("Sorry, the correct answer was Norway.")

    

        
    print("You're final score is: " + str(score))
    percentage = (score / 14) *100
    print("You got " + str(percentage) + "%")

christmasQuiz()