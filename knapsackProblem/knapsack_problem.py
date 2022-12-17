import random
from abc import ABC
from simpleai.search import SearchProblem
from simpleai.search.viewers import ConsoleViewer

my_viewer = ConsoleViewer()


class KnapsackProblem(SearchProblem, ABC):
    def __init__(self, number_of_items, knapsack_capacity, weights_of_items, values_of_items):
        initial_state_array = []
        for _ in range(number_of_items):
            initial_state_array.append(0)
        initial_state = tuple(initial_state_array)
        super().__init__(initial_state)
        self.number_of_items = number_of_items
        self.knapsack_capacity = knapsack_capacity
        self.weights_of_items = weights_of_items
        self.values_of_items = values_of_items
        self.current_weights = 0
        self.current_values = 0

    def actions(self, state):
        action_array = []
        for i in range(len(state)):
            if self.is_valid(state, f'Change Item{i}'):
                action_array.append(f'Change Item{i}')

        return action_array

    def is_valid(self, state, action):
        flag = True
        item_value = list(state)
        index = int(action[len(action) - 1: len(action)])
        weight_before_changes = 0
        for _ in range(len(state)):
            weight_before_changes += (item_value[_] * self.weights_of_items[_])  # current weight

        if item_value[index] == 1:
            weight_after_changes = weight_before_changes - (item_value[index] * self.weights_of_items[index])
            item_value[index] = 0
        else:
            item_value[index] = 1
            weight_after_changes = weight_before_changes + (item_value[index] * self.weights_of_items[index])

        if weight_after_changes > self.knapsack_capacity:
            flag = False
        return flag

    def check_weight(self, state):
        weight = 0
        for _ in range(self.number_of_items):
            weight += (state[_] * self.weights_of_items[_])
        return weight

    def result(self, state, action):
        index = int(action[len(action) - 1: len(action)])
        item_value = list(state)
        if item_value[index] == 0:
            item_value[index] = 1
        else:
            item_value[index] = 0
        state = tuple(item_value)
        return state

    def value(self, state):
        self.current_values = 0
        for _ in range(len(state)):
            self.current_values += (state[_] * self.values_of_items[_])
        return self.current_values

    def generate_random_state(self):
        flag = False
        while True:
            random_state = []
            for _ in range(self.number_of_items):
                random_state.append(int(random.uniform(0, 2)))

            random_state_tuple = tuple(random_state)
            '''weight = 0'''
            weight = self.check_weight(random_state_tuple)
            '''for _ in range(len(random_state)):
                weight += (random_state_tuple[_] * self.weights_of_items[_])'''

            if weight <= self.knapsack_capacity:
                flag = True

            if flag:
                break
        return tuple(random_state)

    def mutate(self, state):
        flag = False
        while True:
            item_value = list(state)
            random_index = int(random.uniform(0, self.number_of_items))
            item_value[random_index] = 1 if item_value[random_index] % 2 == 0 else 0
            weight = self.check_weight((tuple(item_value)))
            if weight <= self.knapsack_capacity:
                flag = True
            if flag:
                break
        return tuple(item_value)

    def crossover(self, state1, state2):
        flag = False
        while True:
            crossover_index = int(random.uniform(1, self.number_of_items))
            cross_overed_tuple = state1[:crossover_index] + state2[crossover_index:]
            weight = self.check_weight(cross_overed_tuple)

            if weight <= self.knapsack_capacity:
                flag = True
            if flag:
                break
        return cross_overed_tuple

    def state_representation(self, state):
        return str(state)
