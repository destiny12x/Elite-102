from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Banking App System")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hi there, welcome to your bank!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()



