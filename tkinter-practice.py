# let's build things using the tkinter module
# let's start with a button
# from tkinter import *
# this allows us to call tkinter without having to use it's name every time


from tkinter import *

tk = Tk()
btn = Button(tk, text="click me")
btn.pack()