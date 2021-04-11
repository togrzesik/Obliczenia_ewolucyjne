import numpy as np
import matplotlib.pyplot as plt


class PlotDrawer:

    @staticmethod
    def plot_value_over_generation(file_name, plot_name, values):
        generations = np.arange(1, len(values)+1, 1)

        plt.figure()
        plt.plot(generations, values)
        plt.title(plot_name)
        plt.xlabel('generation')
        plt.ylabel('best')

        plt.savefig(file_name)

