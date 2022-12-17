import knapsack_problem
from simpleai.search import *


def main():
    '''    number_of_items = input('Enter total amount of items: ')
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
        value_of_items.append(value)  '''

    number_of_items = 15
    knapsack_capacity = 50
    weight_of_items = [24, 10, 10, 7, 2, 8, 6, 5, 9, 12, 20, 18, 13, 5, 4]
    value_of_items = [50, 10, 25, 30, 20, 25, 40, 15, 12, 22, 35, 45, 55, 100, 60]

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
