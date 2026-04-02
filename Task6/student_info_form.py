import tkinter as tk
from tkinter import messagebox


def submit():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Name cannot be empty")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number")
        return

    if grade.strip() == "":
        messagebox.showerror("Error", "Grade cannot be empty")
        return

    result = f"Student: {name}\nAge: {age}\nGrade: {grade}"
    result_label.config(text=result)


root = tk.Tk()
root.title("Student Information Form")
root.geometry("300x200")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5, sticky="w")

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
grade_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()