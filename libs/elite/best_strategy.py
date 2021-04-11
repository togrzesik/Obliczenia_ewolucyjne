from libs.elite.best_strategy_base import BestStrategyBase


class BestStrategy:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration;
        self.__number_of_best_chromosomes = self.__algorithm_configuration.selection_amount
        self.__best_strategy_base = BestStrategyBase(self.__algorithm_configuration, self.__number_of_best_chromosomes)

    def get_best_chromosomes(self, population):
        return self.__best_strategy_base.get_best_chromosomes(population)[0]
