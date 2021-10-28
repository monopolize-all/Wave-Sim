import pyglet, numpy

import objects


class Wave_Plot:

    POINTS_TO_PLOT = objects.window.SIZE[0] * 2
    
    def __init__(self, pos, size, x_range, equation, colour = (255, 255, 255)):

        self.window = objects.window

        objects.funcs_to_run_on_draw.append(self.draw)

        self.pos = pos
        self.size = size
        self.x_min, self.x_max = x_range
        self.x_scale = self.size[0] / (self.x_max - self.x_min)
        self.equation = equation
        self.colour = colour

        self.x_values = numpy.linspace(self.x_min, self.x_max, self.POINTS_TO_PLOT)

    def plot(self, **equation_params):

        self.y_values = numpy.fromiter(map(lambda x: self.equation(x, **equation_params), self.x_values), dtype=numpy.float64)

        self.adjusted_x_values = (self.x_values - self.x_min) * self.x_scale + self.pos[0]

        y_min, y_max = min(self.y_values), max(self.y_values)

        self.y_scale = self.size[1] / (y_max - y_min)

        self.adjusted_y_values = (self.y_values - y_min) * self.y_scale + self.pos[1]

        self.points = []
        
        for x, y in zip(self.adjusted_x_values, self.adjusted_y_values):
            self.points.append(x)
            self.points.append(y)

    def draw(self):
        no_of_points = len(self.x_values)
        pyglet.graphics.draw(no_of_points, pyglet.gl.GL_POINTS, 
                            ("v2f", self.points), 
                            ("c3B", self.colour * no_of_points))
