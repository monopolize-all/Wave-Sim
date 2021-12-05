import tkinter, time, math


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


class FloatEntry(tkinter.Entry):

    def __init__(self, master, textvariable):
        super().__init__(master, textvariable = textvariable, validatecommand = self.on_validate)
        vcmd = (self.register(self.on_validate), '%P')
        self.config(validate = "key" ,validatecommand=vcmd)
    
    def validate(self, string):
        try:
            float(string)
            return True
        
        except:
            if string in ("", "-"):
                return True
            return False

    def on_validate(self, P):
        return self.validate(P)    


class Variable_Slider_Widget(tkinter.Frame):

    SLIDER_DEFAULT_LOW = -100
    SLIDER_DEFAULT_HIGH = 100

    def __init__(self, master, text, validate_func = None, result_var = None):
        super().__init__(master)

        self.number_of_values = 100

        self.label = tkinter.Label(self, text = text)
        self.label.grid(column = 0, row = 0)

        if result_var is None:
            self.result_var = tkinter.DoubleVar(self)
            self.result_var.trace_add("write", validate_func)

        else:
            self.result_var = result_var
        
        resolution = self.number_of_values // (self.SLIDER_DEFAULT_HIGH - self.SLIDER_DEFAULT_LOW)
        self.slider = tkinter.Scale(self, variable = self.result_var, from_ = self.SLIDER_DEFAULT_LOW, 
                        to = self.SLIDER_DEFAULT_HIGH, orient = tkinter.HORIZONTAL,
                        resolution = resolution)

        self.slider_low_var = tkinter.DoubleVar(self, value=self.SLIDER_DEFAULT_LOW)
        self.slider_low_var.trace_add("write", self.on_update_low_var)

        self.slider_high_var = tkinter.DoubleVar(self, value=self.SLIDER_DEFAULT_HIGH)
        self.slider_high_var.trace_add("write", self.on_update_high_var)

        self.low_entry = FloatEntry(self, textvariable = self.slider_low_var)
        self.high_entry = FloatEntry(self, textvariable = self.slider_high_var)

        self.low_entry.grid(column = 1, row = 0)
        self.slider.grid(column = 2, row = 0)
        self.high_entry.grid(column = 3, row = 0)

    def on_update_low_var(self, var, indx, mode):
        self.slider.config(from_=self.slider_low_var.get())

    def on_update_high_var(self, var, indx, mode):
        self.slider.config(to_=self.slider_high_var.get())

    def adjust_scale_resolution(self):
        resolution = (self.slider_high_var.get() - self.slider_low_var.get()) / self.number_of_values

        self.slider.configure(resolution = math.ceil(resolution))

    def set_limits(self, low_value, high_value):
        self.slider_low_var.set(low_value)
        self.slider_high_var.set(high_value)

        self.adjust_scale_resolution()

    def set_value(self, value):
        self.result_var.set(value)

    def set_number_of_values(self, value):
        self.number_of_values = value

        self.adjust_scale_resolution()

    def get_value(self):
        return float(self.result_var.get())


class Time_Slider_Widget(tkinter.Frame):

    T_VAR_SPEED_LOW = 0
    T_VAR_SPEED_HIGH = 10

    GRAPH_REFRESH_DEAY_LOW = 10
    GRAPH_REFRESH_DEAY_HIGH = 1000

    def __init__(self, master, root):
        super().__init__(master)

        self.root = root

        self.t_var_speed = 1
        self.graph_refresh_delay = 500
        self.time_at_last_refresh = time.time()

        self.frame1 = tkinter.Frame(self)
        self.frame1.grid(column = 0, row = 0)

        self.label = tkinter.Label(self.frame1, text = "t: ")
        self.label.grid(column = 0, row = 0)

        self.t_var = tkinter.DoubleVar()
        self.t_var_entry = FloatEntry(self.frame1, textvariable = self.t_var)
        self.t_var_entry.grid(column = 1, row = 0)

        self.t_var_speed_slider_widget = Variable_Slider_Widget(self, 
                "Time flow rate(/s): ", validate_func = self.on_t_var_speed_change)
        self.t_var_speed_slider_widget.set_limits(self.T_VAR_SPEED_LOW, self.T_VAR_SPEED_HIGH)
        self.t_var_speed_slider_widget.set_value(self.t_var_speed)
        self.t_var_speed_slider_widget.grid(column = 0, row = 1)

        self.graph_refresh_delay_slider_widget = Variable_Slider_Widget(self, 
                "Graph refresh rate(ms): ", validate_func = self.on_graph_refresh_delay_change)
        self.graph_refresh_delay_slider_widget.set_limits(self.GRAPH_REFRESH_DEAY_LOW, 
                                    self.GRAPH_REFRESH_DEAY_HIGH)
        self.graph_refresh_delay_slider_widget.set_value(self.graph_refresh_delay)
        self.graph_refresh_delay_slider_widget.grid(column = 0, row = 2)

        self.after(int(self.graph_refresh_delay), self.refresh_graph)

    def refresh_graph(self):
        self.after(int(self.graph_refresh_delay), self.refresh_graph)

        if not self.master.master.enabled:
            return

        old_t_var_value = self.t_var.get()
        new_t_value = old_t_var_value + self.t_var_speed * (time.time() - self.time_at_last_refresh)
        self.t_var.set(new_t_value)

        self.time_at_last_refresh = time.time()

        if "t" in self.root.input_frame.equations_input_frame.constants_values:
            self.master.master.constants_values["t"] = new_t_value

        self.master.master.plot_on_graph()

    def on_t_var_speed_change(self, var, indx, mode):
        self.t_var_speed = self.t_var_speed_slider_widget.get_value()

    def on_graph_refresh_delay_change(self, var, indx, mode):
        self.graph_refresh_delay = self.graph_refresh_delay_slider_widget.get_value()

    def get_value(self):
        return self.t_var.get()

    def reset_t_value(self):
        self.t_var.set(0)
        