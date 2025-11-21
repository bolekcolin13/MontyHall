import random as rand

# Code for one-shot Monty Hall game
def montyhall_iter():
    # Define the doors and the parameters of interest
    doors = [1, 2, 3]
    car = rand.choice(doors)
    guess = rand.choice(doors)

    # Define door(s) not of interest
    doors_remaining = [door for door in doors if door != car and door != guess]
    
    # Reveal a goat
    if car == guess:
        door_revealed = rand.choice([door for door in doors if door != guess])
    else: 
        door_revealed = doors_remaining[0]

    # Define the final two doors
    endgame = [door for door in doors if door != door_revealed]

    # Define strategies
    stay_strategy = guess
    switch_strategy = [door for door in endgame if door != guess][0]


    # Define winning conditions
    staywin = (stay_strategy == car)
    switchwin = (switch_strategy == car)

    # Return results of trial
    return staywin, switchwin

# Loop Monty Hall game and present large N proportion data 
def montylooped():
    # Query desired number of trials
    trials = int(input("How many trials would you like to run? "))

    # Initialize variables
    staysuccess = 0
    switchsuccess = 0

    # Run the trials
    for i in range(trials):
        staywin, switchwin = montyhall_iter()
        staysuccess = staysuccess + int(staywin)
        switchsuccess = switchsuccess + int(switchwin)

    stayrate = 100 * (staysuccess / trials)
    switchrate = 100 * (switchsuccess / trials)

    # Return the results
    print(f"The 'Stay' strategy succeeded {staysuccess} times ({stayrate:.2f}%).")
    print(f"The 'Switch' strategy succeeded {switchsuccess} times ({switchrate:.2f}%).")

# Run simulation
montylooped()





