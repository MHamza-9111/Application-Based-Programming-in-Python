import random as r

while True:
    shapes = ["circle","square","rectangle","oval","diamond"]

    attempts = 0

    ai = r.choice(shapes)

    #print(ai)

    print("\nThis Game is Made By Muhammad Hamza Mughal")

    while attempts <= 2:

        user = input("\nEnter Your Guess Shape (circle, square, rectangle, oval, diamond) :").lower()

        if user not in shapes:
            print("\nIncorrect Input! Please Choose From (circle, square, rectangle, oval, diamond")
            continue

        attempts +=1

        if user == ai: 
            print("\nCongrats! You Won The Game...")
            break

        elif attempts == 3:
            print("\nYou Lose! Better Luck Next Time...")

        else:
            print("\nOOPS! Wrong Guess, Try Again. Attempts Left :",3-attempts)
    
    while True:
        PlayAgain = input("\nDo You Want to Play Again? YES/NO :").upper()

        if PlayAgain == "YES":
            break

        elif PlayAgain == "NO":
            print("\nThanks For Playing...")
            exit()

        else:
            print("\nIncorrect Input! Please Choose From (Yes or No)")