import numpy as np

from function import Function


class EliteStrategy:

    def __init__(self, algorithm_configuration, number_of_best_chromosomes):
        self.__number_of_best_chromosomes = number_of_best_chromosomes
        self.__algorithm_configuration = algorithm_configuration
        self.__function = Function(self.__algorithm_configuration)

    def get_best_chromosomes(self, population):
        evaluated_population = self.__function.evaluate_population(population)
        sorted_evaluated_population = evaluated_population.argsort() #this is for max, min: [::-1]

        best_indexes = sorted_evaluated_population[-self.__number_of_best_chromosomes:]
        best_chromosomes = np.take(population, best_indexes, 0)
        new_population_to_evaluate = np.delete(population, best_indexes, 0)

        return best_chromosomes, new_population_to_evaluate