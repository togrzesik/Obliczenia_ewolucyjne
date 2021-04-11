class BaseFileNameGenerator:

    def __init__(self, algorithm_configuration):
        self.__algorithm_configuration = algorithm_configuration

    def get_file_name(self, data):
        return f"SELECTION_{self.__algorithm_configuration.selection_method}_" \
               f"CROSS_{self.__algorithm_configuration.chromosome_config.cross_type}_" \
               f"MUT_{self.__algorithm_configuration.chromosome_config.mut_type}_" \
               f"{data}"