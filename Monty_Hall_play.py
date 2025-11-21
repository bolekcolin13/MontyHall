import random as rand

def montyhall():
    # Define the doors and the parameters of interest
    doors = [1,2,3]
    car = rand.choice(doors)
    
    # Obtain user input for game
    guess = int(input("Enter 1, 2, or 3 to indicate which door you would like to select: "))

    # Define doors NOT of interest
    doors_remaining = [door for door in doors if door != car and door != guess]

    # Reveal a goat
    if car == guess:
        door_revealed = rand.choice([door for door in doors if door != guess])
    else:
        door_revealed =  doors_remaining[0]  

    # Define new doors of interest
    endgame = [door for door in doors if door != door_revealed]
    non_guess = [door for door in endgame if door != guess][0]

    # Monty prompts the user's decision to switch or stay 
    print(f"There was a goat behind door {door_revealed}.")

    decision = input(
        f"""Would you like to switch to door {non_guess}, or would you like to keep your 
        selection of door {guess}? Please type 'switch' or 'stay': """
    ).strip().lower()
    
    # Define success or failure based on initial random assignment and user's decision
    if decision == "switch":
        guess = non_guess
        
    # Return result of game to user
    if guess == car:
        print("Congratulations! You won a brand new car!")
    else:
        print("Womp womp :( I guess you need to go review Bayes' Theorem again.")

montyhall()