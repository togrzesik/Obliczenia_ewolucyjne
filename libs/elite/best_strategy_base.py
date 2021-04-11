import numpy as np

from libs.algorithm.function import Function


class BestStrategyBase:

    def __init__(self, algorithm_configuration, number_of_best_chromosomes):
        self.__number_of_best_chromosomes = number_of_best_chromosomes
        self.__algorithm_configuration = algorithm_configuration
        self.__function = Function(self.__algorithm_configuration)

    def get_best_chromosomes(self, population):
        if self.__number_of_best_chromosomes is 0:
            return [], []

        evaluated_population = self.__function.evaluate_population(population)
        sorted_evaluated_population = evaluated_population.argsort()
        optimization_evaluated_population = \
            self.__get_sorted_evaluated_population_for_optimization(sorted_evaluated_population)

        best_indexes = optimization_evaluated_population[-self.__number_of_best_chromosomes:]
        best_chromosomes = np.take(population, best_indexes, 0)
        new_population_to_evaluate = np.delete(population, best_indexes, 0)

        return best_chromosomes, new_population_to_evaluate

    def __get_sorted_evaluated_population_for_optimization(self, evaluated_population):
        if self.__algorithm_configuration.is_maximization:
            return evaluated_population

        return evaluated_population[::-1]
