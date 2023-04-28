import numpy as np
from numpy.random import normal


def evo_sim_plast_DynTheta(pop_size, num_generations, r, K, a, initial_theta, mu, sigma, fitness_threshold, v, pR):
    """
    Simulate the evolution of a quantitative trait in a population over a given number of generations
    with a time-dependent optimum trait value (theta) and plastic tolerance range (pR).

    Parameters
    ----------
    pop_size : int
        Size of the population.
    num_generations : int
        Number of generations to simulate.
    r : float
        Maximum fitness at low density with an optimal phenotype.
    K : float
        Carrying capacity.
    a : float
        Strength of stabilizing selection.
    initial_theta : float
        Initial optimal trait value for an environment.
    mu : float
        Mean of the initial population distribution.
    sigma : float
        Standard deviation of the initial population distribution.
    fitness_threshold : float
        Minimum fitness required for an individual to survive and reproduce.
    v : float
        Rate of environmental change.
    pR : float
        Plastic tolerance range, the equidistant range around the trait value where the fitness
        is not affected by stabilizing selection.

    Returns
    -------
    mean_trait : list
        List of mean trait values per generation.
    population_size : list
        List of population sizes per generation.
    mean_fitness : list
        List of mean fitness values per generation.
    """
    # Initialize population
    pop = np.random.normal(loc=mu, scale=sigma, size=pop_size)

    # Simulate evolution
    mean_trait = []
    population_size = []
    mean_fitness = []
    for gen in range(num_generations):
        # Update optimal trait value based on time
        theta = initial_theta + v * gen

        # Calculate centerDist
        centerDist = pop - theta

        # Calculate the expressed trait value based on the centerDist and pR
        expressed_trait = np.where(np.abs(centerDist) > pR, centerDist - np.sign(centerDist) * pR, 0) + theta


        # Calculate fitness based on the new fitness calculation
        w = r * (1 - (pop_size / K)) - (a / 2) * expressed_trait**2
        w = np.exp(w)  # Convert to probability

        # Survival and reproduction based on fitness threshold
        survivors = pop[w >= fitness_threshold]
        if len(survivors) == 0:
            # Extinction occurs
            break

        w = w[w >= fitness_threshold]
        w /= np.sum(w)

        # Select parents
        parents = np.random.choice(survivors, size=len(survivors), p=w, replace=True)

        # Create offspring + ADD PERTURBATION HERE !!!
        offspring = np.random.normal(loc=parents, scale=sigma, size=len(parents))

        # Update population
        pop = offspring
        pop_size = len(pop)

        # Store mean trait, population size, and mean fitness
        mean_trait.append(np.mean(pop))
        population_size.append(pop_size)
        mean_fitness.append(np.mean(w))

    return mean_trait, population_size, mean_fitness
