from tkinter import *

window = Tk()
window.geometry("480x360+50+50")
window.title("Grid Manager")

#Begin placing your widgets here

txt1 = Entry(bd=2)
txt1.grid(row=0, column=0, sticky=N)
txt1.insert(0, "row 0 column 0")
txt2 = Entry(bd=2)
txt2.grid(row=0, column=1)
txt2.insert(0, "row 0  column 1")
txt3 = Entry(bd=2)
txt3.grid(row=0, column=2)
txt3.insert(0, "row 0 column 2")
txt4 = Entry(bd=2)
txt4.grid(row=1, column=0)
txt4.insert(0, "row 1 column 0")
txt5 = Entry(bd=2)
txt5.grid(row=1, column=1)
txt5.insert(0, "row 1 column 1")
txt6 = Entry(bd=2)
txt6.grid(row=1, column=2)
txt6.insert(0, "row 1 column 2")

window.mainloop()