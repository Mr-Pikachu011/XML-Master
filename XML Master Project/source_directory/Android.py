from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage

# ------------------------ TextView ------------------------


def textview(layout, android_layout_width, android_layout_height, android_text, android_textSize=10, android_textStyle="", android_textColor="black", android_background="white", android_layout_marginTopBottom=0, android_layout_marginLeftRight=0):
    l1 = Label(layout, text=android_text, font=(
        "Arial", android_textSize, android_textStyle), bg=android_background, fg=android_textColor, pady=android_layout_marginTopBottom, padx=android_layout_marginLeftRight)
    l1.place(x=android_layout_width, y=android_layout_height)


# ------------------------ EditText ------------------------

def edittext(layout, android_layout_width, android_layout_height, android_textSize=10, android_textStyle="", android_textColor="black", android_background="white"):
    l1 = Entry(layout, font=(
        "Arial", android_textSize, android_textStyle), bg=android_background, fg=android_textColor)
    l1.place(x=android_layout_width, y=android_layout_height)


# ------------------------ Button ------------------------

def button(layout, android_layout_width, android_layout_height, android_text, android_textSize=10, android_textStyle="", android_textColor="black", android_background="white", android_layout_marginTopBottom=0, android_layout_marginLeftRight=0):
    l1 = Button(layout, text=android_text, font=(
        "Arial", android_textSize, android_textStyle), bg=android_background, fg=android_textColor, pady=android_layout_marginTopBottom, padx=android_layout_marginLeftRight)
    l1.place(x=android_layout_width, y=android_layout_height)


# ------------------------ Image ------------------------

def imageview(layout, android_layout_width, android_layout_height, android_src, android_layout_marginTopBottom=0, android_layout_marginLeftRight=0, android_width=0, android_height=0):
    l2 = Label(layout, image=android_src, pady=android_layout_marginTopBottom,
               padx=android_layout_marginLeftRight, height=android_height, width=android_width)
    l2.place(x=android_layout_width, y=android_layout_height)


# ------------------------ Toggle Button ------------------------

def off():
    toggle_photo.configure(file="off.png")
    toggle_button.configure(command=on)


def on():
    toggle_photo.configure(file="on.png")
    toggle_button.configure(command=off)


def togglebutton(layout, android_layout_width, android_layout_height, android_textSize=10, android_textStyle="", android_layout_marginTopBottom=0, android_layout_marginLeftRight=0):
    global toggle_button, toggle_photo
    toggle_photo = PhotoImage(file="on.png")
    toggle_button = Button(layout, image=toggle_photo, border=0, font=(
        "arial", android_textSize, android_textStyle), command=off, padx=android_layout_marginLeftRight, pady=android_layout_marginTopBottom)
    toggle_button.place(x=android_layout_width, y=android_layout_height)


# ------------------------ Radio Button ------------------------

def radiobutton(layout, android_layout_width, android_layout_height, android_text, android_values, android_textSize=10, android_textStyle="", android_layout_marginTopBottom=0, android_layout_marginLeftRight=0):
    r1 = Radiobutton(layout, text=android_text, value=android_values, font=(
        "Arial", android_textSize, android_textStyle), pady=android_layout_marginTopBottom, padx=android_layout_marginLeftRight,)
    r1.place(x=android_layout_width, y=android_layout_height)


# ------------------------ Check Button ------------------------

def checkbutton(layout, android_layout_width, android_layout_height, android_text, android_textSize=10, android_textStyle="", android_layout_marginTopBottom=0, android_layout_marginLeftRight=0):
    r1 = Checkbutton(layout, text=android_text,  font=(
        "Arial", android_textSize, android_textStyle), pady=android_layout_marginTopBottom, padx=android_layout_marginLeftRight,)
    r1.place(x=android_layout_width, y=android_layout_height)

