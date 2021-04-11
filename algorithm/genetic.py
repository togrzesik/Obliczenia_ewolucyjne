from algorithm.genetic_algorithm import GeneticAlgorithm
from generator.base_file_name_generator import BaseFileNameGenerator
from o.file_writer import FileWriter
from plot.plot_drawer import PlotDrawer


class Genetic:

    def __init__(self, alg_config):
        self.__gen_alg = GeneticAlgorithm(alg_config)
        self.__base_file_name_generator = BaseFileNameGenerator(alg_config)
        self.__file_writer = FileWriter()
        self.__plot_drawer = PlotDrawer()

        decoded_best_chromosome, solution_best_value, list_best, list_mean, list_std, elapsed_time \
            = self.__gen_alg.evolve()

        self.__decoded_best_chromosome = decoded_best_chromosome
        self.__solution_best_value = solution_best_value
        self.__elapsed_time = elapsed_time

        list_best_file_name = self.__base_file_name_generator.get_file_name('list_best')
        self.__file_writer.write_value_over_generation(list_best_file_name + '.txt', list_best)
        self.__plot_drawer.plot_value_over_generation(list_best_file_name + '.png', 'list_best', list_best)

        list_best_file_name = self.__base_file_name_generator.get_file_name('list_mean')
        self.__file_writer.write_value_over_generation(list_best_file_name + '.txt', list_best)
        self.__plot_drawer.plot_value_over_generation(list_best_file_name + '.png', 'list_mean', list_best)

        list_best_file_name = self.__base_file_name_generator.get_file_name('list_std')
        self.__file_writer.write_value_over_generation(list_best_file_name + '.txt', list_best)
        self.__plot_drawer.plot_value_over_generation(list_best_file_name + '.png', 'list_std', list_best)

    @property
    def decoded_best_chromosome(self):
        return self.__decoded_best_chromosome

    @property
    def solution_best_value(self):
        return self.__solution_best_value

    @property
    def elapsed_time(self):
        return self.__elapsed_time