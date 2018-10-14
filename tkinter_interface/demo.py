import tkinter
from tkinter import messagebox


mainapp = tkinter.Tk()
mainapp.title("Windows tkinter")
# mainapp.minisize(x, y)
# mainapp.maxsize(x, y)
# mainapp.resizable(width=False, height=True)
mainapp.geometry("800x600+50+100")


label = tkinter.Label(mainapp, text="Hello world")
label.config(text='New Message')


def callback_entry_on_change(*args):
    label.config(text=var_label.get())


"""
No save on press papier
"""
var_label = tkinter.StringVar()
var_label.trace('w', callback_entry_on_change)
entry = tkinter.Entry(mainapp, exportselection=0, show="0", textvariable=var_label)

def hello():
    messagebox.showinfo("Hello title", "Welcome")

button = tkinter.Button(mainapp, text='okok', width=20, command=hello)



entry.pack()
label.pack()
button.pack()
mainapp.mainloop()