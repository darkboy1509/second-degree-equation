import tkinter as tk
from tkinter import messagebox
from math import sqrt

def solve_equation():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        messagebox.showerror("Error", "The equation has no real solutions.")
    elif discriminant == 0:
        x = -b / (2*a)
        messagebox.showinfo("Solution", f"The solution is x = {x}.")
    else:
        x1 = (-b + sqrt(discriminant)) / (2*a)
        x2 = (-b - sqrt(discriminant)) / (2*a)
        messagebox.showinfo("Solution", f"The solutions are x = {x1} and x = {x2}.")
    # Step by step solution
    messagebox.showinfo("Step by step solution", f'Discriminant = {b}^2 - 4*{a}*{c} = √{discriminant}')
    if discriminant > 0:
        messagebox.showinfo("Step by step solution", f'x1 = (-{b} + √{discriminant}) / (2*{a}) = {x1}')
        messagebox.showinfo("Step by step solution", f'x2 = (-{b} - √{discriminant}) / (2*{a}) = {x2}')

def clear():
    a_entry.delete(0,tk.END)
    b_entry.delete(0,tk.END)
    c_entry.delete(0,tk.END)
    
def reset():
    a_entry.delete(0,tk.END)
    b_entry.delete(0,tk.END)
    c_entry.delete(0,tk.END)
    a_entry.insert(0,"0")
    b_entry.insert(0,"0")
    c_entry.insert(0,"0")
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Second Degree Equation Solver")
root.protocol("WM_DELETE_WINDOW", on_closing)

a_label = tk.Label(root, text="Enter the coefficient of x^2:")
a_label.grid(row=0, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1)

b_label = tk.Label(root, text="Enter the coefficient of x:")
b_label.grid(row=1, column=0)
b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1)

c_label = tk.Label(root, text="Enter the constant:")
c_label.grid(row=2, column=0)
c_entry = tk.Entry(root)
c_entry.grid(row=2, column=1)

#Create the solve button

solve_button = tk.Button(root, text="Solve", command=solve_equation)
solve_button.grid(row=3, column=0)

#Create the clear button

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=1)

#Create the reset button

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=3, column=2)

#Create the quit button

quit_button = tk.Button(root, text="Quit", command=on_closing)
quit_button.grid(row=4, column=1)

root.mainloop()