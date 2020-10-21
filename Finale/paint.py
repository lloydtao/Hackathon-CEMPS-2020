from tkinter import Tk, Canvas, Button, Frame, PhotoImage, ROUND, TRUE
from tkinter.colorchooser import askcolor


class Paint:
    def __init__(self):
        self.root = Tk()

        self.c = Canvas(self.root, bg="white", width=320, height=320)
        self.c.grid(row=1, columnspan=1)

        self.color_button = Button(self.root, text="color", command=self.choose_color)
        img = PhotoImage(file="button-colour.gif")
        self.color_button.grid(row=0, column=0)
        self.color_button.config(image=img)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.line_width = 3
        self.color = "black"
        self.eraser_on = False

        self.old_x = None
        self.old_y = None

        self.c.bind("<B1-Motion>", self.paint)
        self.c.bind("<ButtonRelease-1>", self.reset)

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]

    def paint(self, event):
        paint_color = "white" if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(
                self.old_x,
                self.old_y,
                event.x,
                event.y,
                width=self.line_width,
                fill=paint_color,
                capstyle=ROUND,
                smooth=TRUE,
                splinesteps=36,
            )
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == "__main__":
    Paint()
