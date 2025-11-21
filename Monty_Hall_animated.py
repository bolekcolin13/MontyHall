import random as rand
import matplotlib.pyplot as plt
import numpy as np

def montyhall():
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
    switchstrategy = [door for door in endgame if door != guess][0]

    # Define winning conditions 
    staywin = (stay_strategy == car)
    switchwin = (switchstrategy == car)

    # Return results of trial
    return staywin, switchwin

# Loop Monty Hall game and present large N proportion data 
def montylooped():
    # Query desired number of trials
    trials = int(input("How many trials would you like to run? "))

    # Initialize variables
    switchsuccess = 0

    # Initialize arrays to be populated via trials and then plotted
    trials_array = [] # for x-axis
    switch_wins_prop = [] # for graph of proportion of switch wins over time
    switch_wins_total = [] # for graph of total switch wins over time

    # Loop and input results into arrays
    for i in range(1, (trials + 1)):
        staywin, switchwin = montyhall()
        switchsuccess += int(switchwin)

        trials_array.append(i)
        switch_wins_prop.append(switchsuccess/(i))
        switch_wins_total.append(switchsuccess)

    # Return desired arrays
    return np.array(trials_array), np.array(switch_wins_prop), np.array(switch_wins_total)

# Define a function to retrieve and plot the stored arrays
def visuals():
    # Assign returned values from montylooped() to callable variables
    xpoints, ypoints_prop, ypoints_total = montylooped()
    trial_total = xpoints[-1]
    switch_total = ypoints_total[-1]

    # Interactive feature so both figures can be shown simultaneously
    plt.ion()

    # Define proportion graph
    plt.figure(figsize = (10,5))
    plt.plot(xpoints, ypoints_prop, label = "Proportion of Switch Wins", color = "black")
    plt.ylim(0,1) # hard-code the total proportion space 
    plt.axhline((2/3), color = "red", linestyle = "--", label = "Expected Probability")
    plt.xlabel("Number of Trials")
    plt.ylabel(f"Proportion of Switch Successes in {trial_total} Trials")
    plt.title("Proportion of Switch Successes over Time in the Monty Hall Problem")
    plt.legend()
    plt.show() 

    # Define total graph
    plt.figure(figsize = (10,5))
    plt.bar(xpoints, ypoints_total, label = "Total Switch Wins", color = "black")
    plt.ylim(0, trial_total) # hard-code the y-axis
    plt.plot([0,trial_total], [0, switch_total], color = "red", linestyle = "--", label = "Expected Density") # slope with 2/3 slope for reference
    plt.xlabel("Number of Trials")
    plt.ylabel(f"Total Number of Switch Successes in {trial_total} Trials")
    plt.title("Total Switch Success over Time in the Monty Hall Problem")
    plt.legend()
    plt.show(block=True) # to allow both graphs to show at the same time

visuals()

