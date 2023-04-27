import numpy as np

def ou_update(traits, theta, sigma):
    # traits: current trait values
    # theta: mean-reversion parameter of the OU process
    # sigma: volatility parameter of the OU process

    # calculate the mean trait value
    mean_trait = np.mean(traits)

    # calculate the OU process update
    ou_update = theta * (mean_trait - traits) + sigma * np.random.normal(0, 1, len(traits))

    return ou_update


def lande_evolution_ou(N, h2, s, mu, theta, sigma, generations):
    # N: initial population size
    # h2: heritability of the trait
    # s: selection coefficient
    # mu: mutation rate
    # theta: OU process mean-reversion parameter
    # sigma: OU process volatility parameter
    # generations: number of generations to simulate

    # initialize the population with random trait values
    traits = np.random.normal(0, 1, N)

    # initialize the OU process
    ou = np.zeros(N)

    for gen in range(generations):
        # calculate the fitness of each individual
        fitness = np.exp(s * traits) / np.mean(np.exp(s * traits))

        # calculate the mean trait value and fitness of the population
        mean_trait = np.mean(traits)
        mean_fitness = np.mean(fitness)

        # calculate the breeding values of each individual
        bv = (1 - h2) * np.mean(traits) + h2 * traits

        # sample new individuals from the population with replacement
        new_traits = np.random.choice(traits, size=N, replace=True)

        # add mutation to the new individuals
        new_traits += np.random.normal(0, mu, N)

        # calculate the fitness of the new individuals
        new_fitness = np.exp(s * new_traits) / np.mean(np.exp(s * new_traits))

        # calculate the OU process update
        ou = ou_update(traits, theta, sigma)

        # update the traits with the OU process and selection
        traits = traits + ou + bv * (new_fitness - fitness)

    return len(traits), np.mean(traits), np.mean(np.exp(s * traits))
