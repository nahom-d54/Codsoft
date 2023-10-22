import tkinter as tk

class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")

        # Create an Entry widget to display the input and result
        self.entry = tk.Entry(self, width=25, justify="right", font=("Arial", 14))
        self.entry.grid(row=0, column=0,columnspan=4,rowspan=2)

        # Create buttons for numbers and operators
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("/", 4, 3),
            ("C", 5, 0), ("Back", 5, 1)  # New buttons for clearing and backspace
        ]

        for button_text, row, column in buttons:
            
            button = tk.Button(
                self, text=button_text, width=6, height=2,font=("Arial", 12),
                command=lambda text=button_text: self.handle_button_click(text)
            )
            
            button.grid(row=row+1, column=column)

    def handle_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                self.handle_button_click('C')
                self.entry.insert(tk.END, str(result))
            except:
                self.handle_button_click('C')
                self.entry.insert(tk.END, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)  # Clear the entry
        elif text == "Back":
            if self.entry.get() == "Error":
                self.handle_button_click('C')
            self.entry.delete(len(self.entry.get()) - 1, tk.END)  # Delete the last character
        else:
            if self.entry.get() == "Error":
                return
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    calculator = CalculatorUI()
    calculator.mainloop()