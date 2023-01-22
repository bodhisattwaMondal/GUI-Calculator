# Calculator GUI Program using Tkinter Module 
from tkinter import *

root = Tk()
root.geometry("340x510")
root.maxsize(340,510)
root.minsize(340,510)
root.title("Calculator by Bodhi")
root.wm_iconbitmap("1.ico")


def click(event):
    """
    Event Driven Approach.
    This function operates all the underline opeartions for each and every key pressed on the calculator.
    """
    global scvar
    text = event.widget.cget("text")
    if text == '=':
        if scvar.get().isdigit():
            value = int(scvar.get())

        else:
            value = eval(screen.get())

        scvar.set(value)
        screen.update()

    elif text == 'AC':
        scvar.set("")
        screen.update()

    elif text == 'C':
        scvar.set("")
        screen.update()

    else:
        scvar.set(scvar.get() + text)
        screen.update()

# Source Code :

# Creating Frame and variable for Entry Widget and packing the widget

f0 = Frame(root, borderwidth=5, relief = SUNKEN)  # EntryWidget Frame
scvar = StringVar()  # EntryWidget Varible
screen = Entry(f0, textvariable=scvar, font="Lucida 28 bold", bg="grey5", fg="floralwhite")  # EntryWidget 
f0.pack(fill="x")
screen.pack(fill="x",ipady=20)

# Creating 1st frame and packing buttons into it

f1 = Frame(root)
f1.pack(anchor="nw")

b1 = Button(f1, text="AC", font="comicsansms 15 bold", padx=19, bg="grey25", fg="darkgoldenrod1")
b1.pack(side=LEFT, ipady=20)
b1.bind("<Button-1>",click)

b2 = Button(f1, text="C", font="comicsansms 15 bold", padx=30.49900, bg="grey25", fg="darkgoldenrod1")
b2.pack(side=LEFT, ipady=20)
b2.bind("<Button-1>",click)

b3 = Button(f1, text="%", font="comicsansms 15 bold", padx=27.49, bg="grey25")
b3.pack(side=LEFT, ipady=20)
b3.bind("<Button-1>",click)

b4 = Button(f1, text="/", font="comicsansms 15 bold", padx=30, bg="darkorange1", fg="white")
b4.pack(side=LEFT, ipady=20)
b4.bind("<Button-1>",click)

# Creating 2nd frame and packing buttons into it

f2 = Frame(root)
f2.pack(anchor="nw")

b1 = Button(f2, text="7", font="comicsansms 15 bold", padx=27, bg="grey9", fg="snow")
b1.pack(side=LEFT, ipady=20)
b1.bind("<Button-1>",click)

b2 = Button(f2, text="8", font="comicsansms 15 bold", padx=32.2, bg="grey9", fg="snow")
b2.pack(side=LEFT, ipady=20)
b2.bind("<Button-1>",click)

b3 = Button(f2, text="9", font="comicsansms 15 bold", padx=30, bg="grey9", fg="snow")
b3.pack(side=LEFT, ipady=20)
b3.bind("<Button-1>",click)

b4 = Button(f2, text="*", font="comicsansms 15 bold", padx=31, bg="darkorange1", fg="white")
b4.pack(side=LEFT, ipady=20)
b4.bind("<Button-1>",click)

# Creating 3rd frame and packing buttonss into it

f3 = Frame(root)
f3.pack(anchor="nw")

b1 = Button(f3, text="4", font="comicsansms 15 bold", padx=26.5, bg="grey9", fg="snow")
b1.pack(side=LEFT, ipady=20)
b1.bind("<Button-1>",click)

b2 = Button(f3, text="5", font="comicsansms 15 bold", padx=32, bg="grey9", fg="snow")
b2.pack(side=LEFT, ipady=20)
b2.bind("<Button-1>",click)

b3 = Button(f3, text="6", font="comicsansms 15 bold", padx=30, bg="grey9", fg="snow")
b3.pack(side=LEFT, ipady=20)
b3.bind("<Button-1>",click)

b4 = Button(f3, text="-", font="comicsansms 15 bold", padx=32, bg="darkorange1", fg="white")
b4.pack(side=LEFT, ipady=20)
b4.bind("<Button-1>",click)

# Creating 4th frame and packing buttons into it

f4 = Frame(root)
f4.pack(anchor="nw")

b1 = Button(f4, text="1", font="comicsansms 15 bold", padx=26.5, bg="grey9", fg="snow")
b1.pack(side=LEFT, ipady=20)
b1.bind("<Button-1>",click)

b2 = Button(f4, text="2", font="comicsansms 15 bold", padx=32, bg="grey9", fg="snow")
b2.pack(side=LEFT, ipady=20)
b2.bind("<Button-1>",click)

b3 = Button(f4, text="3", font="comicsansms 15 bold", padx=30, bg="grey9", fg="snow")
b3.pack(side=LEFT, ipady=20)
b3.bind("<Button-1>",click)

b4 = Button(f4, text="+", font="comicsansms 15 bold", padx=32, bg="darkorange1", fg="white")
b4.pack(side=LEFT, ipady=20)
b4.bind("<Button-1>",click)

# Creating 5th(last) frame and packing buttons into it

f5 = Frame(root)
f5.pack(anchor="nw")

b1 = Button(f5, text="0", font="comicsansms 15 bold", padx=72,bg="grey9", fg="snow")
b1.pack(side=LEFT, ipady=24)
b1.bind("<Button-1>", click)

b2 = Button(f5, text=".", font="comicsansms 15 bold", padx=33, bg="grey25")
b2.pack(side=LEFT, ipady=24)
b2.bind("<Button-1>", click)

b3 = Button(f5, text="=", font="comicsansms 15 bold", padx=32, bg="orangered", fg="white")
b3.pack(side=LEFT, ipady=24)
b3.bind("<Button-1>", click)

root.mainloop()
