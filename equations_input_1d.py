import tkinter

from equation import Equation
from constants_frame import Constants_Frame


class Equations_Input_1D(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.equations_input_frame = tkinter.Frame(self)
        self.equations_input_frame.grid(column = 0, row = 0)

        tkinter.Label(self.equations_input_frame, text="Equation: ").grid(column = 0, row = 0)

        self.equation_stringvar = tkinter.StringVar()
        self.equation_entry = tkinter.Entry(self.equations_input_frame, textvariable = self.equation_stringvar)
        self.equation_entry.grid(column = 1, row = 0)


        self.generate_parameters_button = tkinter.Button(self, text = "Generate Parameters", 
                        command = self.generate_parameters)

        self.generate_parameters_button.grid(column = 0, row = 1)

        self.equation: Equation

        self.constants_frame = Constants_Frame(self)
        self.constants_frame.grid(column = 0, row = 2)

    def generate_parameters(self):
        self.equation = Equation(self.equation_stringvar.get(), 
                        func_get_constants_values = self.constants_frame.get_constants_values)

        self.constants_frame.clear_constants()

        for constant_name in self.equation.get_constants():
            self.constants_frame.add_constant(constant_name)
