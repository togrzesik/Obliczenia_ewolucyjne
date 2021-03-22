import numpy as np


class TournamentSelection:

    def __init__(self, algorithm_configuration, group_number):
        self.__group_number = group_number
        self.__algorithm_configuration = algorithm_configuration

    def handle_selection(self, population):
        #random
        groups = np.split(population, self.__group_number)

        return groups