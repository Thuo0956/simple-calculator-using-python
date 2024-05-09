from tkinter import *

class Calculator:

    def __init__(self, master):
        master.title("Calculator")
        master.resizable(False, False)
        master.geometry("350x500")
        master.config(bg="greenyellow")
        self.equation = StringVar()
        self.entry_value = ""
        self.entry = Entry(master, width=60, bg="whitesmoke", textvariable=self.equation)
        self.entry.place(x=0, y=0)

        Button(width=11, height=4, text="(", relief="flat", background="blue", command=lambda: self.show("(")).place(x=0, y=50)
        Button(width=11, height=4, text=")", relief="flat", background="blue", command=lambda: self.show(")")).place(x=90, y=50)
        Button(width=11, height=4, text="%", relief="flat", background="blue", command=lambda: self.show("%")).place(x=180, y=50)
        Button(width=11, height=4, text="1", relief="flat", background="blue", command=lambda: self.show("1")).place(x=0, y=125)
        Button(width=11, height=4, text="2", relief="flat", background="blue", command=lambda: self.show("2")).place(x=90, y=125)
        Button(width=11, height=4, text="3", relief="flat", background="blue", command=lambda: self.show("3")).place(x=180, y=125)
        Button(width=11, height=4, text="4", relief="flat", background="blue", command=lambda: self.show("4")).place(x=0, y=200)
        Button(width=11, height=4, text="5", relief="flat", background="blue", command=lambda: self.show("5")).place(x=90, y=200)
        Button(width=11, height=4, text="6", relief="flat", background="blue", command=lambda: self.show("6")).place(x=180, y=200)
        Button(width=11, height=4, text="7", relief="flat", background="blue", command=lambda: self.show("7")).place(x=0, y=275)
        Button(width=11, height=4, text="8", relief="flat", background="blue", command=lambda: self.show("8")).place(x=90, y=275)
        Button(width=11, height=4, text="9", relief="flat", background="blue", command=lambda: self.show("9")).place(x=180, y=275)
        Button(width=11, height=4, text="+", relief="flat", background="blue", command=lambda: self.show("+")).place(x=0, y=350)
        Button(width=11, height=4, text="-", relief="flat", background="blue", command=lambda: self.show("-")).place(x=90, y=350)
        Button(width=11, height=4, text="*", relief="flat", background="blue", command=lambda: self.show("*")).place(x=180, y=350)
        Button(width=11, height=4, text="/", relief="flat", background="blue", command=lambda: self.show("/")).place(x=0, y=425)
        Button(width=11, height=4, text="C", relief="flat", background="blue", command=self.clear).place(x=90, y=425)
        Button(width=11, height=4, text="=", relief="flat", background="blue", command=self.solve).place(x=180, y=425)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except ZeroDivisionError:
            self.equation.set("Error: Division by Zero")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
