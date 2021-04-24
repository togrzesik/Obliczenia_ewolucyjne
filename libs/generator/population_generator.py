import numpy as np


class PopulationGenerator:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration

    def generate_population(self):
        return np.random.randint(2, size=(self.__algorithm_configuration.population_number,
                                          self.__algorithm_configuration.variables_number *
                                          self.__algorithm_configuration.bits_number))

    def generate_real_chromosome_population(self):
        return np.random.uniform(low=self.__algorithm_configuration.left_range_number,
                                 high=self.__algorithm_configuration.right_range_number,
                                 size=(self.__algorithm_configuration.population_number, self.__algorithm_configuration.variables_number))