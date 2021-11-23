import tkinter


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
