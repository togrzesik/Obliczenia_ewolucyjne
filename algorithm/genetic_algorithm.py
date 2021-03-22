import time

import numpy as np

from function import Function
from chromosome.chromosome_decoder import ChromosomeDecoder
from chromosome.cross_service import CrossService
from chromosome.inversion_service import InversionService
from chromosome.mutation_service import MutationService


class GeneticAlgorithm:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__function = Function(self.__algorithm_configuration)
        self.__cross_service = CrossService(self.__algorithm_configuration)
        self.__mutation_service = MutationService(self.__algorithm_configuration)
        self.__inversion_service = InversionService(self.__algorithm_configuration)
        self.__chromosome_decoder = ChromosomeDecoder(self.__algorithm_configuration)

    def evolve(self):
        population = self.__population_generator.generate_population()

        solution_best_value = self.__initialize_solution_best_value()
        solution_best_chromosome = []
        list_best = []
        list_mean = []
        list_std = []

        start = time.time()
        for i in range(self.__algorithm_configuration.epochs_number):
            best_chromosomes, new_population_to_evaluate = self.__elite_strategy.get_best_chromosomes(population)
            population = self.__selection_service.handle_selection(new_population_to_evaluate)
            population = self.__cross_service.handle_cross(population)
            population = self.__mutation_service.handle_mut(population)
            population = self.__inversion_service.handle_inv(population)

            population = np.concatenate((population, best_chromosomes), axis=0)

            evaluated_population = self.__function.evaluate_population(population)
            current_best_chromosome, current_best_chromosome_function_value = \
                self.__function.get_best_chromosome_for_population(population)

            solution_best_chromosome, solution_best_value = \
                self.__update_solution_best_value(solution_best_value, current_best_chromosome_function_value,
                                                  solution_best_chromosome, current_best_chromosome)

            list_best.append(current_best_chromosome_function_value)
            list_mean.append(np.mean(evaluated_population))
            list_std.append(np.std(evaluated_population))

        end = time.time()
        elapsed_time = end - start
        decoded_best_chromosome = self.__chromosome_decoder.decode_chromosome(solution_best_chromosome)

        return decoded_best_chromosome, solution_best_value, list_best, list_mean, list_std, elapsed_time

    def __update_solution_best_value(self, solution_best_value, current_best_chromosome_function_value,
                                     solution_best_chromosome, current_best_chromosome):
        if self.__algorithm_configuration.is_maximization:
            if solution_best_value < current_best_chromosome_function_value:
                solution_best_chromosome = current_best_chromosome
                return solution_best_chromosome, current_best_chromosome_function_value
        else:
            if solution_best_value > current_best_chromosome_function_value:
                solution_best_chromosome = current_best_chromosome
                solution_best_value = current_best_chromosome_function_value

        return solution_best_chromosome, solution_best_value

    def __initialize_solution_best_value(self):
        if self.__algorithm_configuration.is_maximization:
            return -float("inf")

        return float("inf")