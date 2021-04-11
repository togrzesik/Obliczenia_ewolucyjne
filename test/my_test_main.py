from config.algorithm_configuration_provider import AlgorithmConfigurationProvider
from generator.population_generator import PopulationGenerator
from chromosome.chromosome_decoder import ChromosomeDecoder
from algorithm.function import Function
from algorithm.genetic_algorithm import GeneticAlgorithm
from plot.plot_drawer import PlotDrawer

algorithm_configuration = AlgorithmConfigurationProvider(2, 3, 3, 8, 10, True)
population_generator = PopulationGenerator(algorithm_configuration)
population = population_generator.generate_population()
#print(population)
chromosome_decoder = ChromosomeDecoder(algorithm_configuration)
#
#print(chromosome_decoder.decode_chromosome(population[0]))
#print(chromosome_decoder.decode_chromosome(population[1]))
#print(chromosome_decoder.decode_chromosome(population[2]))

function = Function(algorithm_configuration)

#print(function.evaluate_population(population))
#print(function.get_best_chromosome_for_population(population))


#elite_strategy = EliteStrategy(algorithm_configuration, 1)
#print(elite_strategy.get_best_chromosomes(population))

#best_strategy = BestStrategy(algorithm_configuration, 10)
#print(best_strategy.get_best_chromosomes(population))

#tournament_selection = TournamentSelection(algorithm_configuration, 2)
#print(tournament_selection.handle_selection(population))

genetic_algorithm = GeneticAlgorithm(algorithm_configuration)
#print(genetic_algorithm.evolve())
solution_best_value, list_best, list_mean, list_std = genetic_algorithm.evolve()

#file_writer = FileWriter()
#file_writer.write_value_over_generation('list_best.txt', list_best)

plot_drawer = PlotDrawer()
plot_drawer.plot_value_over_generation('best.png', 'best values', list_best)