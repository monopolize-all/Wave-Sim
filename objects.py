import pyglet

from window import Window as window

draw_batch = pyglet.graphics.Batch()

funcs_to_run_on_draw = []

def add_to_draw(func):
    funcs_to_run_on_draw.append(func)

def call_draw():
    for func in funcs_to_run_on_draw:
        func()
