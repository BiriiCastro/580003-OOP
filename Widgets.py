from tkinter import *

window = Tk()

window.geometry("640x480+550+250")
window.title("My first graphical user interface")

btn = Button(text="I am a button", foreground="Red")
btn.place(x=280, y=220)

window.mainloop()
