import tkinter

from input_frame import Input_Frame


class GUI(tkinter.Tk):

    TITLE = "Wave Sim"
    SIZE = (640, 480)

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry("x".join(map(str, self.SIZE)))

        self.input_frame = Input_Frame(self, GUI = self)
        self.input_frame.pack()


if __name__ == "__main__":
    app = GUI()
    app.mainloop()


# a * sin(w1*t+k1*x+c1) + b * sin(w2*t+k2*x+c2) + 200
# 200 * (1 + sin(w*t))
# 100 * (2 + sin(0.2*t+0.05*x))
# 100 * (2 + sin(0.2*t+0.05*x) + sin(0.2*t+0.025*x))

# 200 + 100 * sin(t)
# 200 + 100 * cos(t)
