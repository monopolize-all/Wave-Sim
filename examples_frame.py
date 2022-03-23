import tkinter, json


class Examples_Frame(tkinter.Frame):

    EXAMPLES_FILE_PATH = "examples.json"

    def __init__(self, master, GUI):
        super().__init__(master)

        self.GUI = GUI

        self.next_column = 0

        self.load_examples()

    def load_examples(self):
        with open(self.EXAMPLES_FILE_PATH, "r") as f_handle:
            examples = json.load(f_handle)

        for example_data in examples:
            Example_Button(master = self, GUI = self.GUI, data = example_data).grid(column = self.next_column, row = 0)
            self.next_column += 1


class Example_Button(tkinter.Button):

    def __init__(self, master, GUI, data):
        super().__init__(master, command = self.on_press)

        self.GUI = GUI

        self.data = data

        self.after(0, self.evaluate_data)

    def get_input_frame(self):
        return self.GUI.input_frame

    def evaluate_data(self):
        self.config(text = self.data["text"])
        
    def on_press(self):
        input_frame = self.get_input_frame()

        equation_type = self.data["equation_type"]

        if equation_type == "1D":
            input_frame.equation_type_var.set("1D")

            input_frame.equation_type_selected()

            input_frame.equations_input_frame.equation_stringvar.set(self.data["equation_y"])

        elif equation_type == "2D":
            input_frame.equation_type_var.set("2D")

            input_frame.equation_type_selected()

            input_frame.equations_input_frame.equation_x_stringvar.set(self.data["equation_x"])
            input_frame.equations_input_frame.equation_y_stringvar.set(self.data["equation_y"])

        else:
            raise Exception("Unknown equation type: {}".format(equation_type))
