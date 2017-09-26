# vim: fileencoding=utf-8

import tkinter

def lows():
    tk = tkinter.Tk()
    status = tkinter.Label(tk, text="low status")
    status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    tk.mainloop()

def withRelief():
    tk = tkinter.Tk()
    status = tkinter.Label(tk, text="low status", borderwidth=2, relief="groove")
    status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    tk.mainloop()

def main():
    lows()
    withRelief()

if __name__ == '__main__':
    main()
