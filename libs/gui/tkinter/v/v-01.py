# vim: fileencoding=utf-8

import tkinter
from tkinter.constants import *

def v1():
    tk = tkinter.Tk()
    tk.title("v-01")
    tk.mainloop()

def v2():
    tk = tkinter.Tk()
    tk.title("v-01")
    tk.geometry("30x300+0+0") # w,h,pos,pos
    tk.mainloop()

def v3():
    tk = tkinter.Tk()
    tk.title("v-01")
    tk.geometry("300x300+0+0")
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    label = tkinter.Label(frame, text="v-01")
    label.pack(fill=X, expand=1)
    tk.mainloop()

def v4():
    tk = tkinter.Tk()
    tk.title("v-01")
    tk.geometry("300x300+0+0")
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    button = tkinter.Button(frame, text="exit", command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()


def main():
    v1()
    v2()
    v3()
    v4()

if __name__ == '__main__':
    main()
