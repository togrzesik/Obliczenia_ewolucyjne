from libs.elite.best_strategy import BestStrategy
from libs.selection.roulette_wheel_selection import RouletteWheelSelection
from libs.selection.selection_types import SelectionTypes
from libs.selection.tournament_selection import TournamentSelection


class SelectionService:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration
        self.__best_strategy = BestStrategy(self.__algorithm_configuration)
        self.__roulette_wheel_selection = RouletteWheelSelection(self.__algorithm_configuration)
        self.__tournament_selection = TournamentSelection(self.__algorithm_configuration)

    def handle_selection(self, population):
        return self.__apply_selection(population)

    def __apply_selection(self, population):
        selection_method = self.__algorithm_configuration.selection_method

        if selection_method == SelectionTypes.BEST.name:
            return self.__best_strategy.get_best_chromosomes(population)

        if selection_method == SelectionTypes.ROULETTE.name:
            return self.__roulette_wheel_selection.get_population(population)

        if selection_method == SelectionTypes.TOURNAMENT.name:
            return self.__tournament_selection.handle_selection(population)

