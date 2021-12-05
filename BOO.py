import tkinter

from equation import Equation
from constants_frame import Constants_Frame


class Equations_Input_2D(tkinter.Frame):

    def __init__(self, master, root):
        super().__init__(master)

        self.root: tkinter.Tk = root

        self.parameters_generated = False

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

        self.constants_frame = Constants_Frame(self, root)
        self.constants_frame.grid(column = 0, row = 2)

    def generate_parameters(self):
        self.parameters_generated = True

        self.equation1 = Equation(self.equation1_stringvar.get())

        self.equation2 = Equation(self.equation2_stringvar.get())

        self.constants_frame.clear_constants()

        constants_names = self.equation1.get_constants()
        for constant_name in self.equation2.get_constants():
            if constant_name not in constants_names:
                constants_names.append(constant_name)


        for constant_name in constants_names:
            self.constants_frame.add_constant(constant_name)
