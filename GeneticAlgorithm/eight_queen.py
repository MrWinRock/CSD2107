# Constants, experiment parameters
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import random
from scipy import special as sc

NUM_QUEENS = 8
POPULATION_SIZE = 10
MIXING_NUMBER = 2
MUTATION_RATE = 0.05


def fitness_score(seq):
    score = 0

    for row in range(NUM_QUEENS):
        col = seq[row]

        for other_row in range(NUM_QUEENS):

            # queens cannot pair with itself
            if other_row == row:
                continue
            if seq[other_row] == col:
                continue
            if other_row + seq[other_row] == row + col:
                continue
            if other_row - seq[other_row] == row - col:
                continue
            # score++ if every pair of queens are non-attacking.
            score += 1

    # divide by 2 as pairs of queens are commutative
    return score/2


def selection(population):
    parents = []

    for ind in population:
        # select parents with probability proportional to their fitness score
        if random.randrange(sc.comb(NUM_QUEENS, 2)*2) < fitness_score(ind):
            parents.append(ind)

    return parents


def crossover(parents):

    # random indexes to to cross states with
    cross_points = random.sample(range(NUM_QUEENS), MIXING_NUMBER - 1)
    offsprings = []

    # all permutations of parents
    permutations = list(itertools.permutations(parents, MIXING_NUMBER))

    for perm in permutations:
        offspring = []

        # track starting index of sublist
        start_pt = 0

        # doesn't account for last parent
        for parent_idx, cross_point in enumerate(cross_points):

            # sublist of parent to be crossed
            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)

            # update index pointer
            start_pt = cross_point

        # last parent
        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)

        # flatten the list since append works kinda differently
        offsprings.append(list(itertools.chain(*offspring)))

    return offsprings


def mutate(seq):
    for row in range(len(seq)):
        if random.random() < MUTATION_RATE:
            seq[row] = random.randrange(NUM_QUEENS)

    return seq


def print_found_goal(population, to_print=True):
    for ind in population:
        score = fitness_score(ind)
        if to_print:
            print(f'{ind}. Score: {score}')
        if score == sc.comb(NUM_QUEENS, 2):
            if to_print:
                print('Solution found')
            return True

    if to_print:
        print('Solution not found')
    return False


def evolution(population):
    # select individuals to become parents
    parents = selection(population)

    # recombination. Create new offsprings
    offsprings = crossover(parents)

    # mutation
    offsprings = list(map(mutate, offsprings))

    # introduce top-scoring individuals from previous generation and keep top fitness individuals
    new_gen = offsprings

    for ind in population:
        new_gen.append(ind)

    new_gen = sorted(new_gen, key=lambda ind: fitness_score(
        ind), reverse=True)[:POPULATION_SIZE]

    return new_gen


def generate_population():
    population = []

    for individual in range(POPULATION_SIZE):
        new = [random.randrange(NUM_QUEENS) for idx in range(NUM_QUEENS)]
        population.append(new)

    return population


generation = 0

# generate random population
population = generate_population()

while not print_found_goal(population):
    print(f'Generation: {generation}')
    print_found_goal(population)
    population = evolution(population)
    generation += 1


# checking the mean and stdev of 100,000 random board states
total_sum = []
for i in range(10000):
    population = generate_population()
    for score in list(map(fitness_score, population)):
        total_sum.append(score)

gens = []
for run in range(200):
    generation = 0
    population = generate_population()
    print(f'Run: {run}')
    while not print_found_goal(population, to_print=False):
        population = evolution(population)
        generation += 1

    gens.append(generation)

print(f'Mean: {np.mean(gens)}')
print(f'St. dev: {np.std(gens)}')

print(f'Mean: {np.mean(total_sum)}')
print(f'St. dev: {np.std(total_sum)}')

print(f'Min: {min(gens)}')
print(f'Max: {max(gens)}')

print('Stats from Q1-Q3')
print(f'Min: {min(gens[50:150])}')
print(f'Max: {max(gens[50:150])}')
print(f'Mean: {np.mean(gens[50:150])}')
print(f'St. dev: {np.std(gens[50:150])}')


def reject_outliers(data, m=2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s < m]


no_outliers = reject_outliers(np.array(gens))

print('Removed Outliers')
print(f'Min: {min(no_outliers)}')
print(f'Max: {max(no_outliers)}')
print(f'Mean: {np.mean(no_outliers)}')
print(f'St. dev: {np.std(no_outliers)}')


y = no_outliers

sns.set()
plt.hist(y, bins=np.arange(0, max(no_outliers), 20))
plt.xlabel('Generations to reach solution', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.title('Distribution of Number of Generations to reach solution with a Genetic Algorithm (Outliers removed)', fontsize=24)
plt.rcParams["figure.figsize"] = (20, 10)
plt.xticks(size=15)
plt.yticks(size=15)
plt.axvline(x=np.mean(no_outliers), label='Mean', ls='--')
plt.show()
