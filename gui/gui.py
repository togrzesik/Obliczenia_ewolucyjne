import tkinter as tk
from algorithm_configuration_provider import AlgorithmConfigurationProvider
from mutation_types import MutationTypes
from cross_types import CrossTypes
from selection_types import SelectionTypes


class Gui:
    def __init__(self):
        self.__app = tk.Tk()
        self.__build()

    def open(self):
        self.__app.mainloop()

    def __build(self):
        self.__set_up()
        self.__add_title_label()
        self.__begin_range = self.__add_input_with_label("Begin of the range:")
        self.__end_range = self.__add_input_with_label("End of the range:")
        self.__population_amount = self.__add_input_with_label("Population amount:")
        self.__number_of_bits = self.__add_input_with_label("Number of bits:")
        self.__epochs_amount = self.__add_input_with_label("Epochs amount:")
        self.__best_and_tournament_chromosome_amount = \
            self.__add_input_with_label("Best and tournament chromosome amount:")
        self.__elite_strategy_amount = self.__add_input_with_label("Elite strategy amount:")
        self.__cross_prob = self.__add_input_with_label("Cross probability:")
        self.__mutat_prob = self.__add_input_with_label("Mutation probability:")
        self.__inversion_prob = self.__add_input_with_label("Inversion probability:")
        self.__selection_method = self.__add_drop_down_with_label("Choose selection method:",
                                                                  [option.name for option in SelectionTypes])
        self.__cross_method = self.__add_drop_down_with_label("Choose cross method:",
                                                              [option.name for option in CrossTypes])
        self.__mutation_method = self.__add_drop_down_with_label("Choose mutation method:",
                                                                 [option.name for option in MutationTypes])
        self.__max_or_min_method = self.__add_drop_down_with_label("Choose maximization or minimization method:",
                                                                 ["Maximization", "Minimization"])
        self.__add_button("Start")

    def __button_handler(self):
        is_max = self.__max_or_min_method.get() == "Maximization"
        print(is_max)
        config = AlgorithmConfigurationProvider(float(self.__begin_range.get()),
                                                float(self.__end_range.get()),
                                                int(self.__number_of_bits.get()),
                                                int(self.__population_amount.get()),
                                                int(self.__epochs_amount.get()),
                                                is_max)

    def __add_input_with_label(self, label_name):
        self.__add_label(label_name)
        return self.__add_input()

    def __add_drop_down_with_label(self, label_name, menu_options):
        self.__add_label(label_name)
        return self.__add_drop_down_menu(menu_options)

    def __add_drop_down_menu(self, menu_options):
        variable = tk.StringVar(self.__app)
        variable.set(menu_options[0])
        w = tk.OptionMenu(self.__app, variable, *menu_options)
        self.__set_font_size(w, 14)
        w.pack()
        return variable

    def __add_input(self):
        entry = tk.Entry(fg="white", bg="grey")
        self.__set_font_size(entry, 14)
        entry.pack()
        return entry

    def __add_label(self, string):
        label = tk.Label(
            text=string,
            fg="white",
            bg="black"
        )
        self.__set_font_size(label, 16)
        label.pack()

    def __add_button(self, name):
        button = tk.Button(text=name,
                           fg="white",
                           bg="black",
                           command=self.__button_handler)
        self.__set_font_size(button, 16)
        button.pack()

    def __add_title_label(self):
        label = tk.Label(
            text="Projekt 1 – implementacja klasycznego algorytmu genetycznego",
            fg="white",
            bg="black"
        )
        self.__set_font_size(label, 20)
        label.pack()

    def __set_font_size(self, label, size):
        label.config(font=("Courier", size))

    def __set_up(self):
        self.__set_title()
        self.__set_size()
        self.__set_background()

    def __set_title(self):
        self.__app.title("Projekt 1 - Grzesik, Ksel")

    def __set_size(self):
        self.__app.geometry('1200x900')

    def __set_background(self):
        self.__app.configure(bg="black")
