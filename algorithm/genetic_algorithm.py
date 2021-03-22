import numpy as np

from function import Function
from generator.population_generator import PopulationGenerator


class GeneticAlgorithm:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__population_generator = PopulationGenerator(self.__algorithm_configuration)
        self.__function = Function(self.__algorithm_configuration)

    def evolve(self):
        population = self.__population_generator.generate_population()

        solution_best_value = self.__initialize_solution_best_value()
        list_best = []
        list_mean = []
        list_std = []

        for i in range(self.__algorithm_configuration.epochs_number):
            # elite strategy
            # selection
            # cross
            # mut

            evaluated_population = self.__function.evaluate_population(population)
            current_best_chromosome, current_best_chromosome_function_value = \
                self.__function.get_best_chromosome_for_population(population)

            solution_best_value = self.__update_solution_best_value(solution_best_value,
                                                                    current_best_chromosome_function_value)
            list_best.append(current_best_chromosome_function_value)
            list_mean.append(np.mean(evaluated_population))
            list_std.append(np.std(evaluated_population))

        return solution_best_value, list_best, list_mean, list_std

    def __update_solution_best_value(self, solution_best_value, current_best_chromosome_function_value):
        if self.__algorithm_configuration.is_maximization:
            if solution_best_value < current_best_chromosome_function_value:
                return current_best_chromosome_function_value
        else:
            if solution_best_value > current_best_chromosome_function_value:
                solution_best_value = current_best_chromosome_function_value

        return solution_best_value

    def __initialize_solution_best_value(self):
        if self.__algorithm_configuration.is_maximization:
            return -float("inf")

        return float("inf")