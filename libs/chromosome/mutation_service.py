import numpy as np

from libs.chromosome.chromosome_modifier import ChromosomeModifier
from libs.chromosome.mutation_types import MutationTypes
from representation_types import RepresentationTypes


class MutationService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__chromosome_modifier = ChromosomeModifier(self.__algorithm_configuration.chromosome_config)

    def handle_mut(self, pop_to_mut):
        return [self.__apply_mut(chromosome) for chromosome in pop_to_mut]

    def __apply_mut(self, chromosome):
        chromosome_representation = self.__algorithm_configuration.chromosome_config.representation_type
        mut_type = self.__algorithm_configuration.chromosome_config.mut_type

        if chromosome_representation == RepresentationTypes.BINARY.name:
            if mut_type == MutationTypes.ONE_POINT.name:
                return self.__chromosome_modifier.boundary_mutation_one_point(chromosome)

            if mut_type == MutationTypes.TWO_POINTS.name:
                return self.__chromosome_modifier.boundary_mutation_two_points(chromosome)
        elif chromosome_representation == RepresentationTypes.REAL.name:
            return self.__chromosome_modifier.uniform_mutation(chromosome,
                                                               self.__algorithm_configuration.left_range_number,
                                                               self.__algorithm_configuration.right_range_number)
