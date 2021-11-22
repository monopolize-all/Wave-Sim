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

        tkinter.Label(self, text="Equation: ").grid(column = 0, row = 0)

        self.equation_stringvar = tkinter.StringVar()
        self.equation_entry = tkinter.Entry(self, textvariable = self.equation_stringvar)
        self.equation_entry.grid(column = 1, row = 0)

        self.generate_parameters_button = tkinter.Button(self, text = "Generate Parameters", 
                        command = self.generate_parameters).grid(columnspan = 2, row = 1)

        self.variables_frame = Variable_Frame(self)
        self.variables_frame.grid(columnspan = 2, row = 2)

    def generate_parameters(self):
        self.equation = Equation(self.equation_stringvar.get())

        self.variables_frame.clear_variables()

        for variable_name in self.equation.get_variables():
            self.variables_frame.add_variable(variable_name)


class Variable_Frame(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)
        
        self.variables_widgets = []
        
        # self.add_variable("test")
        # self.add_variable("rest")

        # self.clear_variables()

    def add_variable(self, variable_name):
        row = len(self.variables_widgets)

        label = tkinter.Label(self, text = variable_name + ": ")
        label.grid(column = 0, row = row)

        stringvar = tkinter.StringVar()
        entry = tkinter.Entry(self, textvariable = stringvar)
        entry.grid(column = 1, row = row)

        self.variables_widgets.append([label, entry, stringvar])

    def clear_variables(self):
        for widgets in self.variables_widgets:
            for widget in widgets:
                if hasattr(widget, "destroy"):
                    widget.destroy()

        self.variables_widgets = []


class Equation:

    def __init__(self, string):
        self.evaluate_string(string)
    
    def evaluate_string(self, string):
        """
        raw_string = "".join([char for char in string if not char.isspace()])

        len_raw_string = len(raw_string)

        print(raw_string)

        self.result = raw_string[0]

        if raw_string[1] != "=":
            raise Exception("2nd character is not '='")

        self.variables = []
        """

        self.varibles = [node.id for node in ast.walk(ast.parse(string))
            if type(node) is ast.Name]

    def get_variables(self):
        return self.varibles


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
