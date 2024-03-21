from tkinter import *
from tkinter import ttk, tk

root = Tk()
root.geometry("700x350")

frm = tk.Frame( root, width=500, height=550,style="info.TFrame" )
frm.grid()
# ttk.Label(frm, text='Hello World').grid(column=0,row=0)
# ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
root.mainloop()