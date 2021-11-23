import tkinter, ast


class GUI(tkinter.Tk):

    TITLE = "Wave Sim"
    SIZE = (640, 480)

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry("x".join(map(str, self.SIZE)))

        self.input_frame = Input_Frame(self)
        self.input_frame.pack()


class Input_Frame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)

        tkinter.Label(self, text = "Equation type: ").grid(column = 0, row = 0)

        self.equation_type_var = tkinter.StringVar()

        self.equation_type_frame = tkinter.Frame(self)
        self.equation_type_frame.grid(column = 0, row = 1)

        tkinter.Radiobutton(self.equation_type_frame, text="1D", variable = self.equation_type_var, value="1D",
                        command=self.equation_type_selected).grid(column = 0, row = 0)

        tkinter.Radiobutton(self.equation_type_frame, text="2D", variable = self.equation_type_var, value="2D",
                        command=self.equation_type_selected).grid(column = 1, row = 0)

        self.equations_input_frame = None

        self.equations_input_1D = Equations_Input_1D(self)
        self.equations_input_2D = Equations_Input_2D(self)

    def equation_type_selected(self):
        equation_type = self.equation_type_var.get()

        if equation_type == "1D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_1D.grid(column = 0, row = 2)

            self.equations_input_frame = self.equations_input_1D

        elif equation_type == "2D":
            if self.equations_input_frame is not None:
                self.equations_input_frame.grid_forget()

            self.equations_input_2D.grid(column = 0, row = 2)

            self.equations_input_frame = self.equations_input_2D

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


class Constants_Frame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        self.constants_widgets = []
        self.constants_names = []

        self.deleted_constants_with_values = {}
        
        # self.add_constant("test")
        # self.add_constant("rest")

        # self.clear_constants()

    def add_constant(self, constant_name):
        self.constants_names.append(constant_name)

        row = len(self.constants_widgets)

        label = tkinter.Label(self, text = constant_name + ": ")
        label.grid(column = 0, row = row)

        stringvar = tkinter.StringVar()
        entry = tkinter.Entry(self, textvariable = stringvar)
        entry.grid(column = 1, row = row)

        if constant_name in self.deleted_constants_with_values:
            stringvar.set(self.deleted_constants_with_values[constant_name])

        self.constants_widgets.append([stringvar, label, entry])

    def clear_constants(self):
        self.deleted_constants_with_values = dict(zip(self.constants_names, self.get_constants_values()))

        self.constants_names = []

        for widgets in self.constants_widgets:
            for widget in widgets:
                if hasattr(widget, "destroy"):
                    widget.destroy()

        self.constants_widgets = []

    def get_constants_values(self):
        return [widgets[0].get() for widgets in self.constants_widgets]


class Equation:

    def __init__(self, string, func_get_constants_values):
        self.constants = []
        self.eval_eq_string = ""
        self.func_get_constants_values = func_get_constants_values

        self.evaluate_string(string)
    
    def evaluate_string(self, string):
        """
        raw_string = "".join([char for char in string if not char.isspace()])

        len_raw_string = len(raw_string)

        print(raw_string)

        self.result = raw_string[0]

        if raw_string[1] != "=":
            raise Exception("2nd character is not '='")

        self.constants = []
        """

        eval_eq_string = string.split("=")[1]

        self.constants = [node.id for node in ast.walk(ast.parse(string))
            if type(node) is ast.Name]

        self.constants.pop(0)  # Remove the dependent variable

        f_string_l = list(eval_eq_string)

        start_index = 0

        while start_index < len(f_string_l):
            
            if f_string_l[start_index].isalpha():
                stop_index = start_index

                while stop_index < len(f_string_l) and f_string_l[stop_index].isalpha():
                    stop_index += 1

                f_string_l.insert(start_index, "{")
                f_string_l.insert(stop_index + 1, "}")

                start_index = stop_index + 2

            else:
                start_index += 1

        self.f_eval_eq_string = "".join(f_string_l).lstrip()
        
    def get_constants(self):
        return self.constants

    def solve(self, **variables):
        kwargs = dict(zip(self.constants, self.func_get_constants_values()))
        kwargs.update(variables)

        eval_string = self.f_eval_eq_string.format(**kwargs)

        print(self.f_eval_eq_string, eval_string, sep = "\n")

        return eval(eval_string)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
