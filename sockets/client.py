

import socket
import threading
import tkinter

mainapp = tkinter.Tk()
mainapp.title("Chatter")


def send():
    soc.send(entry.get().encode("utf8")) # we must encode the string to bytes


def receiver(soc):
    while True:
        result_bytes = soc.recv(4096)  # the number means how the response can be in bytes
        result_string = result_bytes.decode("utf8")  # the return will be in bytes, so decode
        label.config(text=result_string)


def setup():
    soc.connect(("", 12345))
    th = threading.Thread(target=receiver, args={soc})
    th.start()


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
label = tkinter.Label(mainapp, text="chat")
entry = tkinter.Entry(mainapp, exportselection=0, show="0")
button = tkinter.Button(mainapp, text='send', width=20, command=send)

setup()

entry.pack()
label.pack()
button.pack()
mainapp.mainloop()