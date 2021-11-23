import tkinter

from input_frame import Input_Frame


class GUI(tkinter.Tk):

    TITLE = "Wave Sim"
    SIZE = (640, 480)

    def __init__(self):
        super().__init__()

        self.title(self.TITLE)
        self.geometry("x".join(map(str, self.SIZE)))

        self.input_frame = Input_Frame(self)
        self.input_frame.pack()


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
