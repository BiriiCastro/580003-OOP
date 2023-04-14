from tkinter import *

class MetricConversion:
    def __init__(self, win):
        self.lbl0 = Label(win, text="Metric Unit of Length", bg="black", fg="white", font=("Times New Roman", 20))
        self.lbl0.place(x=250, y=50)
        self.lbl1 = Label(win, text="Enter the distance in Centimeter(cm): ", bg="black", fg="white")
        self.lbl1.place(x=140, y=120)
        self.lbl2 = Label(win, text="Conversion into Meter(m): ", bg="black", fg="white")
        self.lbl2.place(x=140, y=160)
        self.lbl3 = Label(win, text="Conversion into Kilometer(km): ", bg="black", fg="white")
        self.lbl3.place(x=140, y=200)
        self.ent1 = Entry(win, width=30)
        self.ent1.place(x=360, y=120)
        self.ent2 = Entry(win, width=30)
        self.ent2.place(x=360, y=160)
        self.ent3 = Entry(win, width=30)
        self.ent3.place(x=360, y=200)
        self.btn1 = Button(win, text="Convert", command=self.Converter, width=10, fg="green")
        self.btn1.place(x=325, y=260)
        self.btn2 = Button(win, text="Clear", command=self.Clear, width=10, fg="red")
        self.btn2.place(x=325, y=300)

    def Converter(self):
        self.ent2.delete(0, "end")
        self.ent3.delete(0, "end")
        given = float(self.ent1.get())
        meter = given / 100
        kilometer = given / 100000
        self.ent2.insert(END, "{:.1f}".format(meter))
        self.ent3.insert(END, "{:.3f}".format(kilometer))

    def Clear(self):
        self.ent1.delete(0, "end")
        self.ent2.delete(0, "end")
        self.ent3.delete(0, "end")


window = Tk()
mywin = MetricConversion(window)
window.geometry("720x420+10+10")
window.title("Midterm Exam Problem 02")
window.configure(bg="black")
window.mainloop()
