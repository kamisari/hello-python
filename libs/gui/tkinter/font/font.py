# vim: fileencoding=utf-8

import tkinter
from tkinter import font

def main():
    tk = tkinter.Tk()

    label = tkinter.Label(tk, text="first")
    label.pack(side="top")

    f = font.Font(family="Inconsolate", size=20, weight="bold")
    label2 = tkinter.Label(tk, text="second", bg="blue", fg="white", font=f)
    label2.pack(side="top")

    tk.mainloop()

if __name__ == '__main__':
    main()
