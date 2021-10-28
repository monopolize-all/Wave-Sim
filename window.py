import pyglet

import objects, utility


class Window(pyglet.window.Window):

    SIZE = (500, 500)
    TITLE = "Wave-Sim"

    SHOW_FPS = True

    def __init__(self):
        super().__init__(*self.SIZE, self.TITLE)

        objects.window = self

        width, height = self.SIZE

        self.outline1 = utility.rectangle((10, 10), (width - 20, height - 20), colour = (255, 255, 255))
        self.outline2 = utility.rectangle((11, 11), (width - 22, height - 22), colour = (0, 0, 0))

        self.fps = pyglet.window.FPSDisplay(self)

    def on_draw(self):
        self.clear()
        objects.draw_batch.draw()
        objects.call_draw()

        if self.SHOW_FPS:
            self.fps.draw()
