import numpy as np

from libs.algorithm.function import Function


class TournamentSelection:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__group_members_amount = self.__algorithm_configuration.selection_amount
        self.__function = Function(self.__algorithm_configuration)

    def handle_selection(self, population):
        np.random.shuffle(population)
        groups = self.__split_into_groups(population, self.__group_members_amount)
        best_chromosomes = []
        [best_chromosomes.append(self.__function.get_best_chromosome_for_population(group)[0]) for group in groups]

        return np.array(best_chromosomes)

    @staticmethod
    def __split_into_groups(population, members_amount):
        groups = [population[i * members_amount:(i + 1) * members_amount] for i
                  in range((len(population) + members_amount - 1) // members_amount)]

        return groups
