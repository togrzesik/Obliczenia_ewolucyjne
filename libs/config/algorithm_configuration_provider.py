

class AlgorithmConfigurationProvider:

    def __init__(self, chromosome_config, left_range_number, right_range_number, bits_number, population_number,
                 epochs_number, selection_amount, elite_amount, selection_method, is_maximization):
        self.__chromosome_config = chromosome_config
        self.__left_range_number = left_range_number
        self.__right_range_number = right_range_number
        self.__bits_number = bits_number
        self.__variables_number = 2
        self.__population_number = self.__validate_population_number(population_number)
        self.__epochs_number = epochs_number
        self.__range_dx = self.__calculate_dx()
        self.__selection_amount = selection_amount
        self.__elite_amount = elite_amount
        self.__selection_method = selection_method
        self.__is_maximization = is_maximization

    def __calculate_dx(self):
        if self.__bits_number == 0:
            return 1 / float('inf')
        return (self.__right_range_number - self.__left_range_number) / (2**self.__bits_number - 1)

    def __validate_population_number(self, population_number):
        if self.__bits_number != 0:
            if population_number > 2**(self.__bits_number * self.__variables_number):
                raise Exception('Population number cannot be higher '
                                'than maximum possible numbers that can be encoded binary')
        return population_number

    @property
    def left_range_number(self):
        return self.__left_range_number

    @property
    def right_range_number(self):
        return self.__right_range_number

    @property
    def bits_number(self):
        return self.__bits_number

    @property
    def population_number(self):
        return self.__population_number

    @property
    def range_dx(self):
        return self.__range_dx

    @property
    def epochs_number(self):
        return self.__epochs_number

    @property
    def variables_number(self):
        return self.__variables_number

    @property
    def is_maximization(self):
        return self.__is_maximization

    @property
    def chromosome_config(self):
        return self.__chromosome_config

    @property
    def selection_method(self):
        return self.__selection_method

    @property
    def selection_amount(self):
        return self.__selection_amount

    @property
    def elite_amount(self):
        return self.__elite_amount
