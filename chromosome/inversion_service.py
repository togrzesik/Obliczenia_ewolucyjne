import numpy as np

from chromosome.chromosome_modifier import ChromosomeModifier


class InversionService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_inv(self, pop_to_inv):
        return [self.__chromosome_modifier.inversion(chromosome) for chromosome in pop_to_inv]