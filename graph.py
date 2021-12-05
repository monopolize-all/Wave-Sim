import tkinter

from util import Variable_Slider_Widget

class Graph(tkinter.Toplevel):

    PLOTTER_WIDTH, PLOTTER_HEIGHT = (400, 400)
    BACKGROUND_COLOUR = "#ffffff"
    POINTS_COLOUR = "#000000"

    def __init__(self, master: tkinter.Tk):
        super().__init__(master)

        mx, my = master.winfo_x(), master.winfo_y()
        mw, mh = master.winfo_width(), master.winfo_height()
        x = mx + mw + 10
        y = my

        self.geometry(f"+{x}+{y}")

        self.canvas = tkinter.Canvas(self, bg = self.BACKGROUND_COLOUR, 
                                width = self.PLOTTER_WIDTH, 
                                height = self.PLOTTER_HEIGHT)
        self.canvas.pack()

        self.points_drawn_currently = []

        self.point_radius = 1
        self.point_radius_slider = Variable_Slider_Widget(self, "Pointer radius", 
                                validate_func = self.point_radius_slider_validate)
        self.point_radius_slider.set_limits(1, 20)
        self.point_radius_slider.set_value(1)
        self.point_radius_slider.set_number_of_values(20)
        self.point_radius_slider.pack()

    def point_radius_slider_validate(self, var = None, indx = None, mode = None):
        self.point_radius = self.point_radius_slider.get_value()

        points_to_draw = list(self.points_drawn_currently)

        self.clear_canvas()
        self.draw_points(points_to_draw)        

    def clear_canvas(self):
        self.canvas.delete("all")

        self.points_drawn_currently = []

    def draw_points(self, points):
        for point in points:
            self.draw_point(*point)

    def draw_point(self, x, y):
        self.canvas.create_oval(x, y, x, y, width = self.point_radius, fill = self.POINTS_COLOUR)
        #self.canvas.create_line(x, y, x+1, y, fill = self.POINTS_COLOUR)
        
        self.points_drawn_currently.append((x, y))
