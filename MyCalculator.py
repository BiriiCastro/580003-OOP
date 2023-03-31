from tkinter import *

class MyCalculator:
    def __init__(self, win):
        self.lbl0 = Label(win, text="Calculator", fg="Blue", font=("Taloma", 20))
        self.lbl0.place(x=240, y=30)
        self.lbl1 = Label(win, text="1st No.")
        self.lbl1.place(x=100, y=100)
        self.lbl2 = Label(win, text="2nd No.")
        self.lbl2.place(x=100, y=150)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100, y=200)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=100)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=150)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=200)
        self.btnadd = Button(win, text="Add", fg="Blue", command=self.add)
        self.btnadd.place(x = 200, y = 250)
        self.btnsub = Button(win, text="Subtract", fg="Blue", command=self.sub)
        self.btnsub.place(x=280, y=250)
        self.btnmul = Button(win, text="Multiply", fg="Blue", command=self.mul)
        self.btnmul.place(x=200, y=280)
        self.btndiv = Button(win, text="Divide", fg="Blue", command=self.div)
        self.btndiv.place(x=280, y=280)
        self.clear = Button(win, text="Clear", fg="Red", command=self.clc)
        self.clear.place(x = 400, y= 150)


    def add(self):
        self.txt3.delete(0, "end")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0, "end")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self):
        self.txt3.delete(0, "end")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0, "end")
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 // num2
        self.txt3.insert(END, str(result))

    def clc(self):
        self.txt1.delete(0, "end")
        self.txt2.delete(0, "end")
        self.txt3.delete(0, "end")

window = Tk()
mywin = MyCalculator(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()


