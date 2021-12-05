import tkinter

from equations_input_1d import Equations_Input_1D
from equations_input_2d import Equations_Input_2D
from graph import Graph


class Input_Frame(tkinter.Frame):

    def __init__(self, master, root):
        super().__init__(master)

        self.root = root

        tkinter.Label(self, text = "Equation type: ").grid(column = 0, row = 0)

        self.equation_type_var = tkinter.StringVar()

        self.equation_type_frame = tkinter.Frame(self)
        self.equation_type_frame.grid(column = 0, row = 1)

        tkinter.Radiobutton(self.equation_type_frame, text="1D", variable = self.equation_type_var, value="1D",
                        command=self.equation_type_selected).grid(column = 0, row = 0)

        tkinter.Radiobutton(self.equation_type_frame, text="2D", variable = self.equation_type_var, value="2D",
                        command=self.equation_type_selected).grid(column = 1, row = 0)

        self.equations_input_frame = None

        self.root.after_idle(self.init_widgets)

    def init_widgets(self):
        self.graph = Graph(self.root)

        self.equations_input_1D = Equations_Input_1D(self, self.root, self.graph)
        self.equations_input_2D = Equations_Input_2D(self, self.root, self.graph)

    def equation_type_selected(self):
        equation_type = self.equation_type_var.get()

        if equation_type == "1D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_1D.grid(column = 0, row = 2)

            self.equations_input_frame = self.equations_input_1D
            self.equations_input_1D.enabled = True
            self.equations_input_2D.enabled = False

        elif equation_type == "2D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_2D.grid(column = 0, row = 2)

            self.equations_input_frame = self.equations_input_2D
            self.equations_input_1D.enabled = False
            self.equations_input_2D.enabled = True
