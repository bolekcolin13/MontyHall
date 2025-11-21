# Monty Hall

A number of simulations of the Monty Hall Problem for basic educational purposes. All of the below files feature the problem under its standard rules, i.e., equiprobable assignment of the car to the doors, Monty's complete knowledge of the location of the car, and there being a 50/50 chance of revealing each goat should you happen to choose as a first guess the door behind which is the car.

## Play Monty Hall

The file ```Monty_Hall_play.py``` simulates a one-off instance of the three doors game from the show *Let's Make a Deal.* You don't get much statistical information, but it can be a good introduction to the structure of the game for those who are unfamiliar.

## Monty Hall Trials

The file ```Monty_Hall_trials.py``` is intended to demonstrate the validity of Marilyn vos Savant's argument that made the Monty Hall Problem famous. Say you don't want to teach Bayes' Theorem to any schmuck off the street, or even you just don't want to have to go through the tedium of the math: just run a million or so trials and that should be convincing enough!

## Animated Monty Hall

Intended more so as a pedagogical tool, the file ```Monty_Hall_animated.py``` shows two things: first, it produces a graph demonstrating the convergence of the proportion of successes of the "switch" strategy over an arbitrary number of simulations to $\frac{2}{3}$, consistent with both prediction under Bayes' Theorem and our expectation of sample behavior under the Law of Large Numbers. Second, it produces a bar graph overlayed with a line of slope $\frac{2}{3}$, showing how the number of trials in which the "Switch" strategy was successful out of the arbitrary sample is consistent with our probabilistic expectations.
