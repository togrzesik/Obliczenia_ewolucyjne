import numpy as np


class ChromosomeModifier:

    def __init__(self, chromosome_config):
        self.__chromosome_config = chromosome_config
        self.__boundaries = [0, 1]
        self.ONE_MUTATION = 1
        self.TWO_MUTATIONS = 2

    def cross_one_point(self, tab_a, tab_b):
        if np.random.random() < self.__chromosome_config.cross_prob:
            return self.__cross(tab_a, tab_b)
        else:
            return tab_a, tab_b

    def cross_two_point(self, tab_a, tab_b):
        if np.random.random() < self.__chromosome_config.cross_prob:
            firs_cross_point = np.random.randint(len(tab_a)+1)
            tab_a[0:firs_cross_point], tab_b[0:firs_cross_point] = \
                self.__cross(tab_a[0:firs_cross_point], tab_b[0:firs_cross_point])
            tab_a[firs_cross_point:len(tab_a)], tab_b[firs_cross_point:len(tab_b)] = \
                self.__swap(tab_a[firs_cross_point:len(tab_a)], tab_b[firs_cross_point:len(tab_b)])
        return tab_a, tab_b

    def cross_three_point(self, tab_a, tab_b):
        if np.random.random() < self.__chromosome_config.cross_prob:
            main_cross_point = np.random.randint(len(tab_a) + 1)
            tab_a[0:main_cross_point], tab_b[0:main_cross_point] = \
                self.__cross(tab_a[0:main_cross_point], tab_b[0:main_cross_point])
            tab_a[main_cross_point:len(tab_a)], tab_b[main_cross_point:len(tab_b)] = \
                self.__cross(tab_a[main_cross_point:len(tab_a)], tab_b[main_cross_point:len(tab_b)])
        return tab_a, tab_b

    def cross_homogeneous(self, tab_a, tab_b):
        if np.random.random() < self.__chromosome_config.cross_prob:
            return self.__homogeneous_cross(tab_a, tab_b)
        return tab_a, tab_b

    def cross_arithmetic(self, first, second):
        if np.random.random() < self.__chromosome_config.cross_prob:
            k = np.random.random()
            x1 = first[0]
            y1 = first[1]
            x2 = second[0]
            y2 = second[1]
            x1_new = k * x1 + (1 - k) * x2
            y1_new = k * y1 + (1 - k) * y2
            x2_new = (1 - k) * x1 + k * x2
            y2_new = (1 - k) * y1 + k * y2
            return np.array([x1_new, y1_new]), np.array([x2_new, y2_new])
        return first, second

    def cross_heuristic(self, first, second):
        if np.random.random() < self.__chromosome_config.cross_prob:
            x1 = first[0]
            y1 = first[1]
            x2 = second[0]
            y2 = second[1]
            if x2 > x1 and y2 > y1:
                k = np.random.random()
                x1_new = k * (x2 - x1) + x1
                y1_new = k * (y2 - y1) + y1
                return np.array([x1_new, y1_new])
            return None
        return first

    def __homogeneous_cross(self, tab_a, tab_b):
        for index in range(0, len(tab_a)):
            if np.random.random() < self.__chromosome_config.cross_prob:
                tab_a[index], tab_b[index] = self.__swap(tab_a[index], tab_b[index])
        return tab_a, tab_b

    def __cross(self, tab_a, tab_b):
        cross_point = np.random.randint(len(tab_a) + 1)
        tab_a[0:cross_point], tab_b[0:cross_point] = self.__swap(tab_a[0:cross_point], tab_b[0:cross_point])
        return tab_a, tab_b

    @staticmethod
    def __swap(tab_a, tab_b):
        temp = np.copy(tab_a)
        tab_a = tab_b
        tab_b = temp
        return tab_a, tab_b

    def boundary_mutation_one_point(self, tab):
        if np.random.random() < self.__chromosome_config.mut_prob:
            tab = self.__boundary_mutate_defined_elements(tab, self.ONE_MUTATION)
        return tab

    def boundary_mutation_two_points(self, tab):
        if np.random.random() < self.__chromosome_config.mut_prob:
            return self.__boundary_mutate_defined_elements(tab, self.TWO_MUTATIONS)
        return tab

    def uniform_mutation(self, chromosome, left, right):
        if np.random.random() < self.__chromosome_config.mut_prob:
            index = np.random.randint(2)
            value = np.random.uniform(low=left, high=right)
            chromosome[index] = value
        return chromosome

    def __boundary_mutate_defined_elements(self, tab, mutations_amount):
        for iterator in range(mutations_amount):
            mutated_index = np.random.randint(len(tab))
            tab[mutated_index] = self.__boundary_mutate()
        return tab

    def __boundary_mutate(self):
        if np.random.random() > 0.5:
            return self.__boundaries[1]
        else:
            return self.__boundaries[0]

    def inversion(self, tab):
        if np.random.random() < self.__chromosome_config.inv_prob:
            return self.__invert(tab)
        else:
            return tab

    @staticmethod
    def __invert(tab):
        start = np.random.randint(0, len(tab))
        end = np.random.randint(start, len(tab))
        tab[start:end] = np.flip(tab[start:end])
        return tab




