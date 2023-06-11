from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import glob
import os
from pathlib import Path

def onFrameConfigure(canvas):
	canvas.configure(scrollregion=canvas.bbox("all"))

filepath = os.getcwd() + '/champ_icons/' + '*.png'
a = glob.glob(filepath)
l = len(a)

imgn = []
imagen = []
for i in range(l):
	imgs = 'img' + str(i)
	images = 'image' + str(i)
	imgn.append(imgs)
	imagen.append(images)

root = Tk()
cr = Canvas(root,height=500,width=700)
cv = Canvas(cr,bg="gray25",width=800,height=1150)
vsb = Scrollbar(root,orient="vertical",command=cr.yview)
cr.configure(yscrollcommand=vsb.set)
vsb.pack(side="right",fill="both")
cr.pack()
cr.create_window((0,0),window=cv,anchor="nw")
cv.bind("<Configure>",lambda event,cr=cr:onFrameConfigure(cr))
element = 0
row = 0
column = 0
for filename in glob.glob(filepath):
	a,b = str(filename).split("/")
	c,d = b.split(".")
	z = ""
	for l in range(12,len(c)):
		z = z + c[l]
	print(z)


	imgn[element] = PIL.Image.open(filename)
	imgn[element] = imgn[element].resize((40,40),PIL.Image.ANTIALIAS)
	imagen[element] = ImageTk.PhotoImage(imgn[element],master=root)
	row = int(element/10)
	column = element - row*10
	img = cv.create_image(10+70*column,10+70*row,image=imagen[element],anchor="nw")
	img = cv.create_text(30+70*column,60+70*row,text=z,anchor="center",fill="white",font="calibri 11 bold")
	element = element + 1



root.mainloop()










"""
img = Image.open("champion0.png").convert("RGBA")

w, h = img.size

columns = int(h/48)
rows = int(w/48)

elements = columns * rows
images = []
labels = []
imgn = []

for e in range(elements):
	imge = 'img' + str(e)
	le = 'label' + str(e)
	imagese = 'image' + str(e)

	images.append(imagese)
	labels.append(le)
	imgn.append(imgn)

cv = Canvas(root,width=580,height=200, bg="gray25")
cv.pack()

print(f"{columns} columns, {rows} rows")

t = 0
for i in range(rows):
	for j in range(columns):
		left = 48*i
		right = 48*(i+1)
		upper = 48*j
		lower = 48*(j+1)
		print(i,j)

		imgn[t] = img.crop([left, upper, right, lower])
		images[t] = ImageTk.PhotoImage(imgn[t])
		cv.create_image(53+55*i,50+55*j,image=images[t])
		t = t+1			
"""


