import pyglet

import objects


def rectangle(pos, size, colour = (255, 255, 255)):
    return pyglet.shapes.Rectangle(*pos, *size, color = colour, batch = objects.draw_batch)

def schedule_loop(func, interval):
    pyglet.clock.schedule_interval(func, interval)
