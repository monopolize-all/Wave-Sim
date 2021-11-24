import tkinter

from equation import Equation
from constants_frame import Constants_Frame
from graph import Graph

class Equations_Input_1D(tkinter.Frame):

    TIME_FLOW_RATE_LOW = 0
    TIME_FLOW_RATE_HIGH = 5

    def __init__(self, master, root):
        super().__init__(master)

        self.root: tkinter.Tk = root

        self.parameters_generated = False
        self.constants_values = {}

        self.equations_input_frame = tkinter.Frame(self)
        self.equations_input_frame.grid(column = 0, row = 0)

        tkinter.Label(self.equations_input_frame, text="Equation: ").grid(column = 0, row = 0)

        self.equation_stringvar = tkinter.StringVar()

        self.equation_stringvar.trace_add("write", self.generate_parameters)
        self.equation_entry = tkinter.Entry(self.equations_input_frame, textvariable = self.equation_stringvar)
        self.equation_entry.grid(column = 1, row = 0)

        self.equation: Equation

        self.constants_frame = Constants_Frame(self, root)
        self.constants_frame.grid(column = 0, row = 1)

        self.time_widget = None

        self.error_message_label = tkinter.Label(self, text = "")
        self.error_message_label.grid(column = 0, row = 2)

        self.graph: Graph

        self.root.after_idle(self.init_graph)

    def init_graph(self):
        self.graph = Graph(self.root)

    def show_error_message(self, message):
        self.error_message_label.config(text = message)

    def reset_error_message(self):
        self.error_message_label.config(text = "")

    def generate_parameters(self, var = None, indx = None, mode = None):
        equation_string = self.equation_stringvar.get()

        self.reset_error_message()
        if equation_string == "":
            self.show_error_message("Equation entry empty.")
            return

        elif "=" not in equation_string:
            self.show_error_message("Equation does not have '=' symbol.")
            return

        self.parameters_generated = True

        self.equation = Equation(self.equation_stringvar.get())

        self.constants_frame.clear_constants()

        for constant_name in self.equation.get_constants():
            self.constants_frame.add_constant(constant_name, validate_func = self.on_constants_value_change)

        self.on_constants_value_change()

    def on_constants_value_change(self, var = None, indx = None, mode = None):

        if self.time_widget:
            self.time_widget.reset_t_value()

        all_constants_present = True

        for name, value in zip(self.constants_frame.active_constants_names, 
                    self.constants_frame.get_constants_values()):
            try:
                value = float(value)
                self.constants_values[name] = value
            except:
                all_constants_present = False

        self.reset_error_message()

        if not all_constants_present:
            self.show_error_message("Empty constant field.")

        self.equation.update_constants_values(self.constants_values, all_constants_present)

        self.plot_on_graph()

    def plot_on_graph(self):

        if not (self.equation.solveable and self.equation.all_constants_present):
            return

        points_to_plot = []

        if self.equation.dependent_variable == "y":
            for x in range(self.graph.WIDTH):
                y = self.equation.solve(x=x)
                if y is False:
                    return
                points_to_plot.append([x, y])
        
        self.graph.clear_canvas()
        self.graph.draw_points(points_to_plot)

        return True  # For validation of parameters entry to continue
