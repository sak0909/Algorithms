import random

'''
Simple example for genetic algorithm.
Used genetic evolution (selection and crossover) to find a string. For the given example brute force will be 27^len(answer)
'''

alphabet = "abcdefghijklmnopqrstuvwxyz "

def get_answer():
    return "who is the boss"

def is_answer(a):
    return a == get_answer()

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    c = ""
    for _ in range(size):
        c += get_letter()
    return c

def get_score(chrom):
    key = get_answer()
    cnt = 0
    for i in range(min(len(chrom), len(key))):
        if chrom[i] == key[i]:
            cnt += 1
    return cnt / len(chrom)

def get_mean_score(chromosomes):
    t=0
    for c in chromosomes:
        t += get_score(c)
    return t/len(chromosomes)


def score(chrom):
    # floating number between 0 and 1. The better the chromosome, the closer to 1
    # We coded the get_score(chrom) in the previous exercise
    return get_score(chrom)


def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3  # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    #  * Sort individuals by their fitting score
    #  * Select the best individuals
    #  * Randomly select other individuals
    S = sorted(chromosomes_list, reverse=True, key=score)
    index = int(len(S) * 0.3) + 1
    l = S[:index] + random.sample(S[index:], int(len(S) * 0.2))
    return l

def crossover(parent1, parent2):
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    return parent1[0:int(len(parent1)/2)] + parent2[int(len(parent2)/2): ]


def get_letter():
    return random.choice(alphabet)


def mutation(chrom):
    #  * Random gene mutation : a random gene is replaced with a random char
    ind = random.randrange(len(chrom))

    return chrom[:ind] + get_letter() + chrom[ind + 1:]


def create_population(pop_size, chrom_size):
    # Create random population
    population = []
    for _ in range(pop_size):
        chrom = create_chromosome(chrom_size)
        population.append(chrom)
    return population


def generation(population):
    # selection stage
    # Select the top fitting and a random other members of the population
    select = selection(population)

    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    while len(children) < 1*len(select):
        ## crossover
        ind1 = random.randrange(len(select))
        ind2 = random.randrange(len(select))
        while ind1 != ind2:
            ind2 = random.randrange(len(select))

        parent1 = select[ind1]  # randomly selected
        parent2 = select[ind2]  # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        child = crossover(parent1, parent2)

        ## mutation
        # Mutate on 1% or 1 letter
        for _ in range(max(1, len(child) * 0.01)):
            child = mutation(child)
        children.append(child)
        #print(child)

    # return the new generation
    return select + children


def genetic_algorithm(chrom_size):
    population_size = 20

    # create the base population
    population = create_population(population_size, chrom_size)

    answer = []
    generation_count = 0

    # while a solution has not been found :
    while not answer:
        generation_count+=1
        ## create the next generation
        population = generation(population)

        ## display the average score of the population (watch it improve)
        #print("Mean population score: "+ str(get_mean_score(population)))

        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                # print(chrom)
                answer.append(chrom)

    print("\nAnswer is: "+"".join(answer))
    print("Generation count: " + str(generation_count))


genetic_algorithm(len(get_answer()))