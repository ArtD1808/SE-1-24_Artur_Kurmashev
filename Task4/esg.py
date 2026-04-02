import tkinter as tk
from tkinter import messagebox


def validate_input(raw_text: str) -> float:
    """
    Validates user input:
    - not empty
    - numeric
    - not negative
    Returns: number (float) if valid, otherwise raises ValueError with a clear message.
    """
    text = raw_text.strip()

    if text == "":
        raise ValueError("Input field is empty. Please enter a number.")

    try:
        number = float(text)
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")

    if number < 0:
        raise ValueError("Negative numbers are not allowed. Please enter 0 or a positive number.")

    return number


def calculate_square(number: float) -> float:
    """Calculation logic (Option A): square of a number."""
    return number ** 2


def format_result(value: float) -> str:
    """Formats the output text."""
    return f"Result: {value}"


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Structured Tkinter Calculator")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        # Tkinter variables
        self.input_value = tk.StringVar()
        self.input_value.trace_add("write", self.update_calculate_button_state)

        # Layout container
        self.main_frame = tk.Frame(self.root, padx=15, pady=15)
        self.main_frame.pack(fill="both", expand=True)

        # Widgets
        self.prompt_label = tk.Label(self.main_frame, text="Enter a number:", anchor="w")
        self.prompt_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.input_entry = tk.Entry(self.main_frame, textvariable=self.input_value, width=30)
        self.input_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.calculate_button = tk.Button(
            self.main_frame, text="Calculate", width=14, command=self.on_calculate_click, state="disabled"
        )
        self.calculate_button.grid(row=2, column=0, padx=(0, 8), pady=(0, 10), sticky="w")

        self.clear_button = tk.Button(
            self.main_frame, text="Clear", width=14, command=self.on_clear_click
        )
        self.clear_button.grid(row=2, column=1, pady=(0, 10), sticky="w")

        self.result_label = tk.Label(
            self.main_frame, text="Result: ", fg="black", anchor="w", font=("Arial", 11)
        )
        self.result_label.grid(row=3, column=0, columnspan=2, sticky="w")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

    def update_calculate_button_state(self, *args):
        """UX: Disable Calculate when input is empty."""
        is_empty = self.input_value.get().strip() == ""
        self.calculate_button.config(state="disabled" if is_empty else "normal")

    def show_error(self, message: str):
        """Shows messagebox error with a clear message."""
        messagebox.showerror("Input Error", message)

    def set_result(self, text: str, color: str = "black"):
        """Updates the result label."""
        self.result_label.config(text=text, fg=color)

    # Event handler: ONLY coordinates actions
    def on_calculate_click(self):
        raw_text = self.input_value.get()

        try:
            number = validate_input(raw_text)           # validation in separate function
            result = calculate_square(number)           # calculation in separate function
            self.set_result(format_result(result), "green")
        except ValueError as err:
            self.show_error(str(err))

    # Separate event handler for Clear
    def on_clear_click(self):
        self.input_value.set("")
        self.set_result("Result: ", "black")
        self.update_calculate_button_state()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()