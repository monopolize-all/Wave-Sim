import tkinter

from equation import Equation
from constants_frame import Constants_Frame

class Equations_Input_2D(tkinter.Frame):

    TIME_FLOW_RATE_LOW = 0
    TIME_FLOW_RATE_HIGH = 5

    def __init__(self, master, root, graph):
        super().__init__(master)

        self.root: tkinter.Tk = root

        self.parameters_generated = False
        self.constants_values = {}
        self.plottable = True  # False if unable to plot on graph (error in expression evaluation)
        self.enabled = False  # True when selected in input_frame.py

        self.equations_input_frame = tkinter.Frame(self)
        self.equations_input_frame.grid(column = 0, row = 0)

        tkinter.Label(self.equations_input_frame, text="Parameter x = ").grid(column = 0, row = 0)


        self.equation_x_stringvar = tkinter.StringVar()

        self.equation_x_stringvar.trace_add("write", self.generate_parameters)
        self.equation_x_entry = tkinter.Entry(self.equations_input_frame, textvariable = self.equation_x_stringvar)
        self.equation_x_entry.grid(column = 1, row = 0)


        tkinter.Label(self.equations_input_frame, text="Parameter y = ").grid(column = 0, row = 1)

        self.equation_y_stringvar = tkinter.StringVar()

        self.equation_y_stringvar.trace_add("write", self.generate_parameters)
        self.equation_y_entry = tkinter.Entry(self.equations_input_frame, textvariable = self.equation_y_stringvar)
        self.equation_y_entry.grid(column = 1, row = 1)

        self.equation_x: Equation
        self.equation_y: Equation

        self.constants_frame = Constants_Frame(self, root)
        self.constants_frame.grid(column = 0, row = 1)

        self.time_widget = None

        self.error_message_label = tkinter.Label(self, text = "")
        self.error_message_label.grid(column = 0, row = 2)

        self.graph = graph

    def show_error_message(self, message = ""):
        self.error_message_label.config(text = message)

    def generate_parameters(self, var = None, indx = None, mode = None):
        equation_x_string = self.equation_x_stringvar.get()
        equation_y_string = self.equation_y_stringvar.get()

        self.parameters_generated = True

        self.equation_x = Equation(equation_x_string, error_msg_func = self.show_error_message)
        self.equation_y = Equation(equation_y_string, error_msg_func = self.show_error_message)

        self.constants_frame.clear_constants()

        for constant_name in self.equation_x.get_constants():
            self.constants_frame.add_constant(constant_name, validate_func = self.on_constants_value_change)

        for constant_name in self.equation_y.get_constants():
            self.constants_frame.add_constant(constant_name, validate_func = self.on_constants_value_change)

        self.on_constants_value_change()

        self.plottable = True

    def on_constants_value_change(self, var = None, indx = None, mode = None):

        if self.time_widget:
            self.time_widget.reset_t_value()

        for name, value in zip(self.constants_frame.active_constants_names, 
                    self.constants_frame.get_constants_values()):
            self.constants_values[name] = value

        self.equation_x.update_constants_values(self.constants_values)
        self.equation_y.update_constants_values(self.constants_values)

        self.plot_on_graph()

    def plot_on_graph(self):

        points_to_plot = []

        if not self.plottable:
            return

        x = self.equation_x.solve()
        y = self.equation_y.solve()

        if x is False or y is False:
            self.plottable = False
            self.show_error_message("Invalid expression. (missing '*' perhaps?)")
            return

        self.graph.clear_canvas()
        self.graph.draw_point(x, y)
