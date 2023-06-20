from customtkinter import CTkButton
from Settings import *

# Button
class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span=1, colour="dark_grey"):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING["corner radius"],
            font=font,
            fg_color=COLOURS[colour]["fg"],
            hover_color=COLOURS[colour]["hover"],
            text_color=COLOURS[colour]["text"])

        self.grid(column=col, columnspan=span, row=row, sticky="NSEW", padx=STYLING["gap"], pady=STYLING["gap"])


# Number Buttons (. 0 1 2 3 4 5 6 7 8 9)
class NumButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, colour="light_grey"):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(text),
            col=col,
            row=row,
            span=span,
            font=font,
            colour=colour)


# + - * / +
class SignButton(Button):
    def __init__(self, parent, text, operator, func, col, row, font, colour="orange"):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(operator),
            col=col,
            row=row,
            font=font,
            colour=colour)
