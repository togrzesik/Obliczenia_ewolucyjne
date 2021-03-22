import numpy as np

from chromosome.chromosome_decoder import ChromosomeDecoder


class Function:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_decoder = ChromosomeDecoder(self.__algorithm_configuration)

    @staticmethod
    def evaluate(input_variables):
        x1, x2 = input_variables

        return (1.5 - x1 + x1*x2)**2 + (2.25 - x1 + x1*x2**2)**2 + (2.625 - x1 + x1*x2**3)**2

    def evaluate_chromosome(self, chromosome):
        decoded_chromosome = self.__chromosome_decoder.decode_chromosome(chromosome)

        return self.evaluate(decoded_chromosome)

    def evaluate_population(self, population):
        return np.apply_along_axis(self.evaluate_chromosome, 1, population)

    def get_best_chromosome_for_population(self, population):
        evaluated_population = self.evaluate_population(population)
        index = self.__get_index_for_optimization(evaluated_population)

        return population[index], evaluated_population[index]

    def __get_index_for_optimization(self, evaluated_population):
        if self.__algorithm_configuration.is_maximization:
            return np.argmax(evaluated_population)

        return np.argmin(evaluated_population)