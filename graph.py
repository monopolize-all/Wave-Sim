import tkinter

class Graph(tkinter.Toplevel):

    WIDTH, HEIGHT = (400, 400)
    BACKGROUND_COLOUR = "#ffffff"
    POINTS_COLOUR = "#000000"

    def __init__(self, master: tkinter.Tk):
        super().__init__(master)

        mx, my = master.winfo_x(), master.winfo_y()
        mw, mh = master.winfo_width(), master.winfo_height()
        x = mx + mw + 10
        y = my

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

        self.canvas = tkinter.Canvas(self, bg = self.BACKGROUND_COLOUR, width = self.WIDTH, height = self.HEIGHT)
        self.canvas.pack()

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw_points(self, points):
        for point in points:
            self.draw_point(*point)

    def draw_point(self, x, y):
        self.canvas.create_oval(x, y, x, y, width = 1, fill = self.POINTS_COLOUR)
        #self.canvas.create_line(x, y, x+1, y, fill = self.POINTS_COLOUR)
