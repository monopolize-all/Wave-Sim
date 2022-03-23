import tkinter

from examples_frame import Examples_Frame
from equations_input_1d import Equations_Input_1D
from equations_input_2d import Equations_Input_2D
from graph import Graph


class Input_Frame(tkinter.Frame):

    def __init__(self, master, GUI):
        super().__init__(master)

        self.GUI = GUI

        self.examples_frame = Examples_Frame(master = self, GUI = GUI)
        self.examples_frame.grid(column = 0, row = 0)

        tkinter.Label(self, text = "Equation type: ").grid(column = 0, row = 1)

        self.equation_type_var = tkinter.StringVar()

        self.equation_type_frame = tkinter.Frame(self)
        self.equation_type_frame.grid(column = 0, row = 2)

        tkinter.Radiobutton(self.equation_type_frame, text="1D", variable = self.equation_type_var, value="1D",
                        command=self.equation_type_selected).grid(column = 0, row = 0)

        tkinter.Radiobutton(self.equation_type_frame, text="2D", variable = self.equation_type_var, value="2D",
                        command=self.equation_type_selected).grid(column = 1, row = 0)

        
        # Move origin to center
        self.origin_at_center_frame = tkinter.Frame(self)
        self.origin_at_center_frame.grid(column = 0, row = 3)
        tkinter.Label(self.origin_at_center_frame, text = "Origin at center: ").grid(column = 0, row = 0)

        self.origin_at_center_checkbox_var = tkinter.IntVar()
        tkinter.Checkbutton(self.origin_at_center_frame, command = self.on_origin_at_center_checkbox_check,
                            variable = self.origin_at_center_checkbox_var,
                            onvalue = 1, offvalue = 0).grid(column = 1, row = 0)

        self.equations_input_frame = None
        self.equations_input_frame_row = 4

        self.GUI.after_idle(self.init_widgets)

    def on_origin_at_center_checkbox_check(self):
        self.graph.origin_at_center_bool = self.origin_at_center_checkbox_var.get()

    def init_widgets(self):
        self.graph = Graph(self.GUI)

        self.equations_input_1D = Equations_Input_1D(self, self.GUI, self.graph)
        self.equations_input_2D = Equations_Input_2D(self, self.GUI, self.graph)

    def equation_type_selected(self):
        equation_type = self.equation_type_var.get()

        if equation_type == "1D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_1D.grid(column = 0, row = self.equations_input_frame_row)

            self.equations_input_frame = self.equations_input_1D
            self.equations_input_1D.enabled = True
            self.equations_input_2D.enabled = False

            self.graph.point_radius_slider.set_value(1)

        elif equation_type == "2D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_2D.grid(column = 0, row = self.equations_input_frame_row)

            self.equations_input_frame = self.equations_input_2D
            self.equations_input_1D.enabled = False
            self.equations_input_2D.enabled = True

            self.graph.point_radius_slider.set_value(10)

        try: 
            self.equations_input_frame.plot_on_graph()

        except:
            pass
