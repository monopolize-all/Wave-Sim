import tkinter

from util import Time_Slider_Widget, Variable_Slider_Widget


class Constants_Frame(tkinter.Frame):

    def __init__(self, master, root):
        super().__init__(master)

        self.root = root
        
        self.constants_widgets = {}
        self.active_constants_names = []
        
        # self.add_constant("test")
        # self.add_constant("rest")

        # self.clear_constants()

    def add_constant(self, constant_name, validate_func):
        self.active_constants_names.append(constant_name)

        row = len(self.active_constants_names)

        if constant_name not in self.constants_widgets:
            if constant_name == "t":
                widget = Time_Slider_Widget(self, self.root)

                self.master.time_widget = widget

            else:
                text = constant_name + ": "
                widget = Variable_Slider_Widget(self, text, validate_func = validate_func)
         
            self.constants_widgets[constant_name] = widget
        
        self.constants_widgets[constant_name].grid(column = 0, row = row)

    def clear_constants(self):
        for constant_name in self.active_constants_names:
            self.constants_widgets[constant_name].grid_forget()

        self.active_constants_names = []

    def get_constants_values(self):
        return [self.constants_widgets[constant_name].get_value() for constant_name in self.active_constants_names]

    def get_constants_names(self):
        return self.active_constants_names
