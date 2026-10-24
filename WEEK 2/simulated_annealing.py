import math
import random

def value(x):
    # Objective function to maximize
    return -(x - 5) ** 2 + 25

def simulated_annealing():
    current = int(input("Enter initial state (integer): "))
    temperature = float(input("Enter initial temperature: "))
    cooling_rate = float(input("Enter cooling rate (0 to 1): "))

    while temperature > 0.01:
        next_state = current + random.choice([-1, 1])
        delta = value(next_state) - value(current)

        if delta > 0:
            current = next_state
        else:
            probability = math.exp(delta / temperature)
            if random.random() < probability:
                current = next_state

        temperature *= cooling_rate

    print("Final state:", current)
    print("Final value:", value(current))


simulated_annealing()