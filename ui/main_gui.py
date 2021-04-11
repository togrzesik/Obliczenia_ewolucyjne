from PyQt5.QtCore import Qt, QLocale, QRegExp
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QComboBox, QCheckBox, QMessageBox

from algorithm.genetic import Genetic
from chromosome.cross_types import CrossTypes
from chromosome.mutation_types import MutationTypes
from config.algorithm_configuration_provider import AlgorithmConfigurationProvider
from config.chromosome_config import ChromosomeConfig
from selection.selection_types import SelectionTypes


class MainGui(QWidget):

    def __init__(self):
        super().__init__()
        self.__title = "Genetic Algorithm"
        self.__init_ui()
        self.__form_layout = QFormLayout()
        self.__add_text()
        self.__add_inputs()
        self.__add_selection_method()
        self.__add_cross_method()
        self.__add_mutation_method()
        self.__add_checkbox()
        self.__add_buttons()
        self.setLayout(self.__form_layout)
        self.show()

    def __init_ui(self):
        self.setWindowTitle(self.__title)
        # self.setGeometry(1200, 800, 400, 400)

    def __add_text(self):
        main_text = QLabel()
        main_text.setText("\nGenetic Algorithm for finding max/min in Beale Function\n\n")
        main_text.setAlignment(Qt.AlignHCenter)
        self.__form_layout.addWidget(main_text)

    def __add_inputs(self):
        self.__add_function_property_inputs()
        self.__add_algorithm_property_inputs()
        self.__add_prop_inputs()

    def __add_function_property_inputs(self):
        range_double_validator = QRegExpValidator(QRegExp("[+-]?\\d*[\\.]?\\d+"))

        self.__a_range_input = QLineEdit()
        self.__a_range_input.setPlaceholderText('Begin of the range - a')
        self.__a_range_input.setValidator(range_double_validator)
        self.__form_layout.addRow(self.__a_range_input)

        self.__b_range_input = QLineEdit()
        self.__b_range_input.setPlaceholderText('End of the range - b')
        self.__b_range_input.setValidator(range_double_validator)
        self.__form_layout.addRow(self.__b_range_input)

    def __add_algorithm_property_inputs(self):
        only_int_validator = QIntValidator()

        self.__pop_amount_input = QLineEdit()
        self.__pop_amount_input.setPlaceholderText('Population amount')
        self.__pop_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__pop_amount_input)

        self.__bits_amount_input = QLineEdit()
        self.__bits_amount_input.setPlaceholderText('Number of bits')
        self.__bits_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__bits_amount_input)

        self.__epoch_number_input = QLineEdit()
        self.__epoch_number_input.setPlaceholderText('Epochs amount')
        self.__epoch_number_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__epoch_number_input)

        self.__selection_amount_input = QLineEdit()
        self.__selection_amount_input.setPlaceholderText('Best and tournament chromosome amount')
        self.__selection_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__selection_amount_input)

        self.__elite_amount_input = QLineEdit()
        self.__elite_amount_input.setPlaceholderText('Elite Strategy amount')
        self.__elite_amount_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__elite_amount_input)

    def __add_prop_inputs(self):
        prop_double_validator = QRegExpValidator(QRegExp("0(\\.\\d+)?|1\\.0"))
        self.__cross_prob_input = QLineEdit()
        self.__cross_prob_input.setPlaceholderText('Cross probability')
        self.__cross_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__cross_prob_input)

        self.__mutation_prob_input = QLineEdit()
        self.__mutation_prob_input.setPlaceholderText('Mutation probability')
        self.__mutation_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__mutation_prob_input)

        self.__inversion_prob_input = QLineEdit()
        self.__inversion_prob_input.setPlaceholderText('Inversion probability')
        self.__inversion_prob_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__inversion_prob_input)

    def __add_selection_method(self):
        selection_box_text = QLabel()
        selection_box_text.setText("Choose selection method")

        self.__selection_method_box = QComboBox()
        self.__selection_method_box.addItems(
            [
                SelectionTypes.BEST.name,
                SelectionTypes.ROULETTE.name,
                SelectionTypes.TOURNAMENT.name
            ]
        )
        self.__form_layout.addRow(selection_box_text)
        self.__form_layout.addRow(self.__selection_method_box)

    def __add_cross_method(self):
        cross_box_text = QLabel()
        cross_box_text.setText("Choose cross method")
        self.__cross_method_box = QComboBox()
        self.__cross_method_box.addItems(
            [
                CrossTypes.ONE_POINT.name,
                CrossTypes.TWO_POINTS.name,
                CrossTypes.THREE_POINTS.name,
                CrossTypes.HOMO.name
            ]
        )
        self.__form_layout.addRow(cross_box_text)
        self.__form_layout.addRow(self.__cross_method_box)

    def __add_mutation_method(self):
        mutation_box_text = QLabel()
        mutation_box_text.setText("Choose mutation method")
        self.__mutation_method_box = QComboBox()
        self.__mutation_method_box.addItems(
            [
                MutationTypes.ONE_POINT.name,
                MutationTypes.TWO_POINTS.name
            ]
        )
        self.__form_layout.addRow(mutation_box_text)
        self.__form_layout.addRow(self.__mutation_method_box)

    def __add_checkbox(self):
        self.__max_box = QCheckBox("Maximization", self)
        self.__form_layout.addRow(self.__max_box)

    def __add_buttons(self):
        self.__button = QPushButton("Start")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed())
        self.__form_layout.addRow(self.__button)

    def __handle_button_pressed(self):
        algorithm_config = self.__get_alg_config()
        self.__genetic = Genetic(algorithm_config)
        self.__print_result(self.__genetic)

    @staticmethod
    def __print_result(genetic):
        msg = QMessageBox()
        msg.setWindowTitle("Result")
        msg.setText(f"Found solution in {round(genetic.elapsed_time, 4)} seconds\n\n"
                    f"f({round(genetic.decoded_best_chromosome[0], 4)}, "
                    f"{round(genetic.decoded_best_chromosome[1], 4)})"
                    f" = {round(genetic.solution_best_value, 4)}")
        x = msg.exec_()

    def __get_alg_config(self):
        return AlgorithmConfigurationProvider(
            self.__get_chromosome_config(),
            float(self.__a_range_input.text()),
            float(self.__b_range_input.text()),
            int(self.__bits_amount_input.text()))

    def __get_chromosome_config(self):
        return ChromosomeConfig(
            str(self.__cross_method_box.currentText()),
            str(self.__mutation_method_box.currentText()),
            float(self.__cross_prob_input.text()),
            float(self.__mutation_prob_input.text()),
            float(self.__inversion_prob_input.text())
        )