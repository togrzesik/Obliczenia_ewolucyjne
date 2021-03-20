import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from random import randrange

from libs.chromosome.cross_types import CrossTypes


class CrossService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_cross(self, pop_to_cross):
        pop_to_cross_len = len(pop_to_cross)
        number_of_missing_chromosomes = self.__algorithm_configuration.population_number - pop_to_cross_len - \
                                        self.__algorithm_configuration.elite_amount
        missing_chromosomes = []

        while len(missing_chromosomes) < number_of_missing_chromosomes:
            first_chromosome = pop_to_cross[randrange(pop_to_cross_len)]
            second_chromosome = pop_to_cross[randrange(pop_to_cross_len)]

            first_chromosome, second_chromosome = self.__apply_cross(first_chromosome, second_chromosome)
            missing_chromosomes.append(first_chromosome)
            missing_chromosomes.append(second_chromosome)

        if len(missing_chromosomes) is 0:
            return pop_to_cross

        return np.concatenate((pop_to_cross, missing_chromosomes[0:number_of_missing_chromosomes]), axis=0)

    def __apply_cross(self, first_chromosome, second_chromosome):
        cross_type = self.__algorithm_configuration.chromosome_config.cross_type

        if cross_type == CrossTypes.ONE_POINT.name:
            return self.__chromosome_modifier.cross_one_point(first_chromosome, second_chromosome)

        if cross_type == CrossTypes.TWO_POINTS.name:
            return self.__chromosome_modifier.cross_two_point(first_chromosome, second_chromosome)

        if cross_type == CrossTypes.THREE_POINTS.name:
            return self.__chromosome_modifier.cross_three_point(first_chromosome, second_chromosome)

        if cross_type == CrossTypes.HOMO.name:
            return self.__chromosome_modifier.cross_homogeneous(first_chromosome, second_chromosome)