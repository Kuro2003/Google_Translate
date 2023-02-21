from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# Create a Tk Window
root = Tk()
root.title("Google Galaxy")
root.geometry("500x630")
root.iconbitmap('logo.ico')

# Load background
load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

# Create a text
name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

# Create a box
box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)

# Create a button
button_frame = Frame(root).pack(side=BOTTOM)


def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def translate():
    user_input = box.get(1.0,END)
    t = Translator()
    a = t.translate(user_input,src="vi",dest="en")
    box1.insert(END,a.text)

clear_button = Button(button_frame, text="Clear text", font=(
    "Arial", 10, 'bold'), bg='#303030', fg='#FFFFFF', command=clear)
clear_button.place(x=150, y=310)
translate_button = Button(button_frame, text="Translate", font=(
    "Arial", 10, 'bold'), bg='#303030', fg='#FFFFFF', command=translate)
translate_button.place(x=290, y=310)

box1 = Text(root, width=28, height=10, font=("ROBOTO", 16))
box1.pack(pady=55)


print(googletrans.LANGUAGES)

root.mainloop()
