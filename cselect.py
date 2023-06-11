from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
import os
import pyautogui

def onFrameConfigure(canvas):
	canvas.configure(scrollregion=canvas.bbox("all"))

x,y = pyautogui.position()
root = Tk()

if x <= 1920:
	root.geometry('1600x900+150+100')
elif x>1920:
	root.geometry('1600x900+2070+100')
root.configure(bg = "navy")

a = Label(root,text="aaaaaaaaaaaaaaaaaaaa",bg="red")
a.place(x=300,y=850)

cv = Canvas(root, width=1000, height=700,bg="white")
cv.place(x=300,y=100)

b = Label(cv,text="aaaaaaaaaaaaaaaaaaa",bg="red")
b.place(x=50,y=50)

root.mainloop()