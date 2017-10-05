# vim: fileencoding=utf-8

import tkinter

class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tkinter.Button(self)
        self.button["text"] = "click!"
        self.button["command"] = self.echo
        self.button.pack(side=tkinter.BOTTOM)

        self.quit = tkinter.Button(self, text="quite", command=self.master.destroy)
        self.quit.pack(side=tkinter.BOTTOM)

    def echo(self):
        print("hello")

def main():
    tk = tkinter.Tk()
    app = App(master=tk)
    app.mainloop()

if __name__ == '__main__':
    main()
