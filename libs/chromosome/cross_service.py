import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from random import randrange

from libs.chromosome.cross_types import CrossTypes
from representation_types import RepresentationTypes


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
            x = randrange(pop_to_cross_len)
            first_chromosome = pop_to_cross[randrange(pop_to_cross_len)]
            second_chromosome = pop_to_cross[randrange(pop_to_cross_len)]

            if self.__algorithm_configuration.chromosome_config.representation_type == RepresentationTypes.REAL.name \
                    and self.__algorithm_configuration.chromosome_config.cross_type == CrossTypes.HEURISTIC.name:
                new_chromosome = self.__apply_heuristic_cross(first_chromosome, second_chromosome)
                if new_chromosome is not None:
                    missing_chromosomes.append(new_chromosome)
            else:
                first_chromosome, second_chromosome = self.__apply_cross(first_chromosome, second_chromosome)
                missing_chromosomes.append(first_chromosome)
                missing_chromosomes.append(second_chromosome)

        if len(missing_chromosomes) is 0:
            return pop_to_cross

        return np.concatenate((pop_to_cross, missing_chromosomes[0:number_of_missing_chromosomes]), axis=0)

    def __apply_cross(self, first_chromosome, second_chromosome):
        chromosome_representation = self.__algorithm_configuration.chromosome_config.representation_type
        cross_type = self.__algorithm_configuration.chromosome_config.cross_type

        if chromosome_representation == RepresentationTypes.BINARY.name:
            if cross_type == CrossTypes.ONE_POINT.name:
                return self.__chromosome_modifier.cross_one_point(first_chromosome, second_chromosome)

            if cross_type == CrossTypes.TWO_POINTS.name:
                return self.__chromosome_modifier.cross_two_point(first_chromosome, second_chromosome)

            if cross_type == CrossTypes.THREE_POINTS.name:
                return self.__chromosome_modifier.cross_three_point(first_chromosome, second_chromosome)

            if cross_type == CrossTypes.HOMO.name:
                return self.__chromosome_modifier.cross_homogeneous(first_chromosome, second_chromosome)
        elif chromosome_representation == RepresentationTypes.REAL.name:
            if cross_type == CrossTypes.ARITHMETIC.name:
                return self.__chromosome_modifier.cross_arithmetic(first_chromosome, second_chromosome)

    def __apply_heuristic_cross(self, first_chromosome, second_chromosome):
        return self.__chromosome_modifier.cross_heuristic(first_chromosome, second_chromosome)
