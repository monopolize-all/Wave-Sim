import tkinter

from equation import Equation
from constants_frame import Constants_Frame


class Equations_Input_2D(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.equations_input_frame = tkinter.Frame(self)
        self.equations_input_frame.grid(column = 0, row = 0)

        tkinter.Label(self.equations_input_frame, text="Equation 1: ").grid(column = 0, row = 0)
        self.equation1_stringvar = tkinter.StringVar()
        self.equation1_entry = tkinter.Entry(self.equations_input_frame, 
                                textvariable = self.equation1_stringvar)
        self.equation1_entry.grid(column = 1, row = 0)

        tkinter.Label(self.equations_input_frame, text="Equation 2: ").grid(column = 0, row = 1)
        self.equation2_stringvar = tkinter.StringVar()
        self.equation2_entry = tkinter.Entry(self.equations_input_frame, 
                                textvariable = self.equation2_stringvar)
        self.equation2_entry.grid(column = 1, row = 1)


        self.generate_parameters_button = tkinter.Button(self, text = "Generate Parameters", 
                        command = self.generate_parameters)

        self.generate_parameters_button.grid(column = 0, row = 1)

        self.equation1: Equation
        self.equation2: Equation

        self.constants_frame = Constants_Frame(self)
        self.constants_frame.grid(column = 0, row = 2)

    def generate_parameters(self):
        self.equation1 = Equation(self.equation1_stringvar.get(), 
                        func_get_constants_values = self.constants_frame.get_constants_values)

        self.equation2 = Equation(self.equation2_stringvar.get(), 
                        func_get_constants_values = self.constants_frame.get_constants_values)

        self.constants_frame.clear_constants()

        for constant_name in self.equation1.get_constants():
            self.constants_frame.add_constant(constant_name)

        for constant_name in self.equation2.get_constants():
            self.constants_frame.add_constant(constant_name)
