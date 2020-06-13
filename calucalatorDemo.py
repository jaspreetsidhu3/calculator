from tkinter import *

button1 = []
button2 = []
for i in range(8, -1, -1):
    button1.append(i)
    # print(i)

for i in range(5,-1,-1):
    button2.append(i)
    print(i)
def data(event):
    value = event.widget.cget("text")

    if (value == "="):

        if ("+" in Data.get()):
            v = Data.get().split("+")
            Data.set(int(v[0]) + int(v[1]))
            print(v)
        if ("-" in Data.get()):
            v = Data.get().split("-")
            Data.set(int(v[0]) - int(v[1]))
            print(v)
    if (value != "=" and value != "C"):
        Data.set(Data.get() + value)
        editText.update()
    if (value == "C"):
        Data.set(int(int(Data.get()) / 10))
        editText.update()


i = 0


def change():
    global i
    i = i + 1
    if (i % 2 == 0):
        Cvalue.set("LightMode")
        root.config(bg="black")
        button2[5].update()
        for k in range(8, -1, -1):
            button1[k].config(bg="black", fg="white")
        for k in range(5,-1,-1):
            button2[k].config(bg="black", fg="white")
        editText.config(bg="black", fg="white")
    else:
        Cvalue.set("Darkmode")
        button2[5].update()
        root.config(bg="white")
        editText.config(bg="white", fg="black")
        for k in range(8, -1, -1):
            button1[k].config(bg="white", fg="black")
        for k in range(5,-1,-1):
            button2[k].config(bg="white", fg="black")
        editText.config(bg="white", fg="black")

root = Tk()
Cvalue = StringVar()
Cvalue.set("DarkMode")
button2[5] = Button(root, textvariable=Cvalue, command=change)
button2[5].pack(anchor=W)
root.geometry("500x700")
root.title("Developed by JASPREET SINGH")
root.maxsize(500, 700)
root.minsize(500, 700)
Data = StringVar()
Data.set("")
editText = Entry(root, font="lucida 60 bold", textvariable=Data)
editText.pack(fill=X, ipady=8, pady=40)
frame = Frame(root)

for i in range(9, 6, -1):
    button1[9 - i] = Button(frame, text=f"{i}", font="lucida 30 bold", pady=8, padx=52)
    button1[9 - i].pack(side=LEFT)
    button1[9 - i].bind('<Button-1>', data)
frame.pack()
frame = Frame(root)
for i in range(6, 3, -1):
    button1[9 - i] = Button(frame, text=f"{i}", font="lucida 30 bold", pady=8, padx=52)
    button1[9 - i].pack(side=LEFT)
    button1[9 - i].bind('<Button-1>', data)
frame.pack()
frame = Frame(root)
for i in range(3, 0, -1):
    button1[9 - i] = Button(frame, text=f"{i}", font="lucida 30 bold", pady=8, padx=52)
    button1[9 - i].pack(side=LEFT)
    button1[9 - i].bind('<Button-1>', data)
frame.pack()
frame = Frame(root)
button2[0] = Button(frame, text="0", font="lucida 30 bold", pady=8, padx=52)
button2[0].pack(side=LEFT)
button2[0].bind('<Button-1>', data)
button2[1] = Button(frame, text="-", font="lucida 30 bold", pady=8, padx=52)
button2[1].pack(side=LEFT)
button2[1].bind('<Button-1>', data)
button2[2] = Button(frame, text="+", font="lucida 30 bold", pady=8, padx=52)
button2[2].pack(side=LEFT)
button2[2].bind('<Button-1>', data)
frame.pack()
frame = Frame(root)
button2[3] = Button(frame, text="=", font="lucida 30 bold", pady=8, padx=52)
button2[3].pack(side=RIGHT)
button2[3].bind('<Button-1>', data)
button2[4] = Button(frame, text="C", font="lucida 30 bold", pady=8, padx=52)
button2[4].pack(side=RIGHT)
button2[4].bind('<Button-1>', data)
frame.pack()
root.mainloop()
