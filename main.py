import tkinter


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

    def generate_parameters(self):
        self.equation = Equation(self.equation_stringvar.get())


class Equation:

    OPERATORS = [
        "+",
        "-",
        "/",
        "*",
        "%"
    ]

    def __init__(self, string):
        self.evaluate_string(string)
    
    def evaluate_string(self, string):

        raw_string = "".join([char for char in string if not char.isspace()])

        len_raw_string = len(raw_string)

        print(raw_string)

        self.result = raw_string[0]

        if raw_string[1] != "=":
            raise Exception("2nd character is not '='")

        self.variables = []

        index = 2
        while index < len_raw_string:
            
            next_operator_index = index

            while next_operator_index < len_raw_string and raw_string[next_operator_index] not in self.OPERATORS:
                next_operator_index += 1

            

            index = next_operator_index + 1


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
