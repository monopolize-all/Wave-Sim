"""
Wave-Sim - A python application to display wave equations.
Made using Python 3 and Pyglet.
Made by: Mohit Mohandas
"""


import pyglet, math

import objects, utility

from window import Window

from wave_plot import Wave_Plot


window = Window()


def real_of_e_pow_i(thetha):
    return math.cos(thetha)

def eq1(x, A = 1, B = 0, k1 = 1, alpha = 0, t = 0):
    return A * real_of_e_pow_i(k1 * x + t) + B * real_of_e_pow_i(-k1 * x)

wave1 = Wave_Plot((20, 20), (460, 460), (-math.pi, math.pi), eq1)

t = 0
def main_loop(dt):
    global t
    t += 0.05
    wave1.plot(t = t)

FPS = 60
utility.schedule_loop(main_loop, 1/FPS)


if __name__ == "__main__":
    pyglet.app.run()
