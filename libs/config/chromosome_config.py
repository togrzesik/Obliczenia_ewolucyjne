
class ChromosomeConfig:

    def __init__(self, cross_type, mut_type, cross_prob, mut_prob, inv_prob):
        self.__cross_type = cross_type
        self.__mut_type = mut_type
        self.__cross_prob = cross_prob
        self.__mut_prob = mut_prob
        self.__inv_prob = inv_prob

    @property
    def cross_type(self):
        return self.__cross_type

    @property
    def mut_type(self):
        return self.__mut_type

    @property
    def cross_prob(self):
        return self.__cross_prob

    @property
    def mut_prob(self):
        return self.__mut_prob

    @property
    def inv_prob(self):
        return self.__inv_prob

