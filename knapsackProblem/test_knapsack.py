import knapsack_problem
from simpleai.search import *


def main():
    number_of_items = input('Enter total amount of items: ')
    number_of_items = int(number_of_items)
    knapsack_capacity = input('Enter knapsack capacity: ')
    knapsack_capacity = int(knapsack_capacity)
    weight_of_items = []
    value_of_items = []
    for _ in range(number_of_items):
        weight = input(f'Enter weight of item{_}: ')
        weight = int(weight)
        weight_of_items.append(weight)

    for _ in range(number_of_items):
        weight = input(f'Enter value of item{_}: ')
        value = int(weight)
        value_of_items.append(value)

    #  result = hill_climbing_random_restarts(problem, 10, 10, viewer=knapsack_problem.my_viewer)
    #  result = hill_climbing(problem=problem, iterations_limit=0, viewer=knapsack_problem.my_viewer)
    problem = knapsack_problem.KnapsackProblem(number_of_items=number_of_items,
                                               knapsack_capacity=knapsack_capacity,
                                               weights_of_items=weight_of_items,
                                               values_of_items=value_of_items)

    result = genetic(problem=problem, population_size=100, mutation_chance=0.1,
                     iterations_limit=0, viewer=knapsack_problem.my_viewer)

    print(result.state)
    print(f'Value: {result.value}')
    print(f'Weight: {problem.check_weight(result.state)}')


if __name__ == '__main__':
    main()
