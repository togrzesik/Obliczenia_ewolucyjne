import numpy as np

from algorithm.function import Function


class RouletteWheelSelection:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__function = Function(self.__algorithm_configuration)
        self.__is_max_opt = self.__algorithm_configuration.is_maximization

    def get_population(self, old_pop):
        old_pop = np.sort(old_pop)
        eval_pop = self.__function.evaluate_population(old_pop)
        if not self.__is_max_opt:
            eval_pop = 1/eval_pop
        corrected_eval_pop = eval_pop + abs(eval_pop.min())
        wheel = np.cumsum(corrected_eval_pop)
        new_pop = []
        for el in np.random.rand(self.__algorithm_configuration.selection_amount):
            new_pop.append(old_pop[(wheel > el * wheel.max())][0])
        return np.array(new_pop)