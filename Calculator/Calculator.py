# Imports
import customtkinter as ctk
import darkdetect
from Buttons import Button, NumButton, SignButton
from Settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self, is_dark):

        # Setup
        super().__init__(fg_color=(WHITE, BLACK))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title("")
        self.iconbitmap("images/empty.ico")
        self.title_bar_colour(is_dark)

        self.rowconfigure(list(range(ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(COLUMNS)), weight=1, uniform="a")

        # Data
        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")
        self.display_num = []
        self.full_operation = []

        # Widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # Font
        main_font = ctk.CTkFont(family=FONT, size=MAIN_FONT_SIZE)
        results_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        # Output labels
        OutputLabel(self, 0, "SE", main_font, self.formula_string)  # Formula
        OutputLabel(self, 1, "E", results_font, self.result_string)  # Results

        # Operator Buttons (Clear/AC, Invert/INV, Percent/%
        def operators(parent=self, font=main_font):
            Button(parent=parent,
                   func=self.clear,
                   text=OPERATORS["clear"]["text"],
                   col=OPERATORS["clear"]["col"],
                   row=OPERATORS["clear"]["row"],
                   font=font)
            Button(parent=parent,
                   func=self.invert,
                   text=OPERATORS["invert"]["text"],
                   col=OPERATORS["invert"]["col"],
                   row=OPERATORS["invert"]["row"],
                   font=main_font)
            Button(parent=parent,
                   func=self.percent,
                   text=OPERATORS["percent"]["text"],
                   col=OPERATORS["percent"]["col"],
                   row=OPERATORS["percent"]["row"],
                   font=font)

        def numbers(parent=self, font=main_font):
            for num, data in NUMBER_POSITIONS.items():
                NumButton(
                    parent=parent,
                    text=num,
                    func=self.num_pressed,
                    col=data["col"],
                    row=data["row"],
                    span=data["span"],
                    font=font)

        def signs(parent=self, font=main_font):
            for sign, data in MATH_POSITIONS.items():
                SignButton(
                    parent=parent,
                    text=data["character"],
                    func=self.sign_pressed,
                    operator=sign,
                    col=data["col"],
                    row=data["row"],
                    font=font)

        operators()
        numbers()
        signs()

    def clear(self):
        self.result_string.set(0)
        self.formula_string.set("")

        self.display_num.clear()
        self.full_operation.clear()

    def percent(self):
        if self.display_num:

            current_num = float("".join(self.display_num))
            percent_num = current_num / 100

            self.display_num = list(str(percent_num))
            self.result_string.set("".join(self.display_num))


    def invert(self):
        current_num = "".join(self.display_num)
        if current_num:

            if float(current_num) > 0:
                self.display_num.insert(0, "-")
            else:
                del self.display_num[0]

            self.result_string.set("".join(self.display_num))

    def num_pressed(self, num):
        self.display_num.append(str(num))
        full_num = "".join(self.display_num)
        self.result_string.set(full_num)

    def sign_pressed(self, sign):
        current_num = "".join(self.display_num)

        if current_num:
            self.full_operation.append(current_num)

            if sign != "=":
                self.full_operation.append(sign)
                self.display_num.clear()

                self.result_string.set("")
                self.formula_string.set(" ".join(self.full_operation))

            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)

                # Format Result
                if isinstance(result, float):

                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 4)

                # Updated Data
                self.full_operation.clear()
                self.display_num = [str(result)]

                # Updated Output
                self.result_string.set(result)
                self.formula_string.set(formula)

    def title_bar_colour(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOUR = TITLE_BAR_HEX_COLOURS["dark"] if is_dark else TITLE_BAR_HEX_COLOURS["light"]
            windll.dwampi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOUR)), sizeof(c_int))
        except:
            pass


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)


if __name__ == "__main__":
    Calculator(darkdetect.isDark())
