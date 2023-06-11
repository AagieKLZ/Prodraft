from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import glob
import os
from pathlib import Path

def onFrameConfigure(canvas):
	canvas.configure(scrollregion=canvas.bbox("all"))


def FilterIcons(*args):
	r = searching.get().upper()
	searching.set(r)
	DeleteIcons()
	row = 0
	column = 0
	element = 0
	global names
	for filename in glob.glob(filepath):
		a,b = str(filename).split("/")
		c,d = b.split(".")
		z = ""
		for l in range(12,len(c)):
			z = z + c[l]
		if searching.get().capitalize() in z or searching.get().lower() in z:
			names.append(z)
			imgn[element] = PIL.Image.open(filename)
			imgn[element] = imgn[element].resize((40,40),PIL.Image.ANTIALIAS)
			imagen[element] = ImageTk.PhotoImage(imgn[element],master=root)
			row = int(element/14)
			column = element - row*14
			icons[element] = cv.create_image(300+70*column,800+70*row,image=imagen[element],anchor="nw")
			cv.tag_bind(icons[element],"<Button-1>",owo)
			if len(z) > 8:
				f = "calibri 8 bold"
			else:
				f="calibri 9 bold"
			nametags[element] = cv.create_text(320+70*column,850+70*row,text=z.upper(),anchor="center",fill="white",font=f)
			element = element + 1


def DeleteIcons():
	global names
	names = []
	for i in range(len(icons)):
		cv.unbind("<Button-1>")
		cv.delete(icons[i])
		cv.delete(nametags[i])

def GetPosition(i):
	if i == 0:
		w,h = 150,330
	elif i ==1:
		w,h = 875,330
	elif i ==2:
		w,h=265,330
	elif i ==3:
		w,h=990,330
	elif i ==4:
		w,h=380,330
	elif i ==5:
		w,h=1105,330
	elif i == 6:
		w,h=150,100
	elif i == 7:
		w,h=875,100
	elif i ==8:
		w,h=990,100
	elif i ==9:
		w,h=265,100
	elif i ==10:
		w,h=380,100
	elif i == 11:
		w,h=1105,100
	elif i == 12:
		w,h=1220,330
	elif i == 13:
		w,h=495,330
	elif i == 14:
		w,h=1335,330
	elif i == 15:
		w,h=610,330
	elif i == 16:
		w,h=1220,100
	elif i == 17:
		w,h=495,100
	elif i == 18:
		w,h=610,100
	elif i == 19:
		w,h=1335,100

	return w,h

def owo(event):
	SelectB.configure(state='active',relief='raised')
	SelectB.configure(bg="gray25",fg="white")
	x = event.x
	y = event.y
	columnmax = int((x+20-270-40)/70)
	columnmin = int((x-20-270-40)/70)
	global phase, n

	row = int((y-800)/70)
	if columnmax == columnmin:
		column = columnmin
	else:
		column = columnmax
	n = column + row * 14
	
	fnames = []
	imgz = []
	imagenz = []

	if names[n] not in picks and selection[phase] == 1 and phase <19:
		picks.append(names[n])
	elif selection[phase] == 0 and names[n] not in picks and phase <19:

		try:
			picks[len(picks)-1] = names[n]
		except:
			picks.append(names[n])

	for j in range(len(picks)):
		imgz.append('img'+str(j))
		imagenz.append('image'+str(j))

	r = 0

	for i in range(len(picks)):
		try:
			fname = os.getcwd() + '/splasharts/' + picks[i] + '.png'
			load = PIL.Image.open(fname)
			load = load.resize((115,210),PIL.Image.ANTIALIAS)
			render = ImageTk.PhotoImage(load,master=root)
			img = Label(cv,image=render,bg="gray5")
			img.Image = render
			w,h=GetPosition(i)
			img.place(x=w,y=h)
		except:
			pass

	if selection[phase] == 1 and len(picks)>phase and phase < 19:
		phase = phase + 1
		root.after_cancel(after_id)

def timercheck():
	if selection[phase]==0:
		countdown(30)

def ResetTimer():
	global after_id
	global timerblue
	global timerred
	timerblue['text'] = ""
	timerred['text'] = ""
	root.after_cancel(after_id)
	countdown(30)

def SelectPick():
	global phase
	global selection
	global picks
	global n
	selection[phase]=1
	SelectB.configure(state='disabled',relief='sunken')
	SelectB.configure(bg="gray25",fg="white")
	ResetTimer()

def countdown(count):
	global phase
	global after_id
	bluephases = [0,2,4,13,15,6,9,10,17,18]
	redphases = [1,3,4,12,14,7,8,11,16,19]
	print(phase)
	if phase in bluephases:
		timerblue['text'] = count
	elif phase in redphases:
		timerred['text'] = count
	if count > 0:
		after_id = root.after(1000,countdown,count-1)

	if count == 0:
		if phase in bluephases:
			timerblue['text'] = ""
		elif phase in redphases:
			timerred['text'] = ""
		SelectPick()



filepath = os.getcwd() + '/champ_icons/' + '*.png'
a = glob.glob(filepath)
l = len(a)

global root, cr, cv
global picks
global names
global phase
global searching
phase = 0
picks = []
names = []
imgn = []
imagen = []
icons = []
nametags = []
for i in range(l):
	imgs = 'img' + str(i)
	images = 'image' + str(i)
	imgn.append(imgs)
	imagen.append(images)
	icons.append('icon'+str(i))
	nametags.append('tag'+str(i))

root = Tk()
root.geometry('+0+0')
root.resizable(0,0)
root.title('Prodraft')

cr = Canvas(root,height=1000,width=1600)
cv = Canvas(cr,bg="gray5",width=1600,height=1650)
vsb = Scrollbar(root,orient="vertical",command=cr.yview)
cr.configure(yscrollcommand=vsb.set)
vsb.pack(side="right",fill="both")
cr.pack()
cr.create_window((0,0),window=cv,anchor="nw")
cv.bind("<Configure>",lambda event,cr=cr:onFrameConfigure(cr))
element = 0
row = 0
column = 0

#cv.create_rectangle(150,10,610+115,80,fill="grey25")
cv.create_polygon(170,10,745,10,725,80,150,80,fill="grey25")
cv.create_polygon(855,10,1430,10,1450,80,875,80,fill="grey25")
cv.create_polygon(675,10,745,10,725,80,655,80,fill="medium blue")
cv.create_polygon(855,10,875,80,945,80,925,10,fill="firebrick1")

global selection
selection = [0]*20

timerblue = Label(cv,font="calibri 36 bold",bg="grey25",fg = "white")
timerblue.place(x=600,y=10)
#countdown(5)

timerred = Label(cv,font="calibri 36 bold",bg="grey25",fg="white")
timerred.place(x=1000,y=10)
#countdown(5)

root.after(1,timercheck)

searching = StringVar()
search = Entry(cv,textvar=searching,font="calibri 11 bold")
search.place(x=670,y=750,width=150,height=25)
searching.trace_add('write',FilterIcons)

SelectB = Button(cv,text="SELECT",font="calibri 11 bold",fg="white",bg="gray25",command=SelectPick)
SelectB.place(x=830,y=750,width=100,height=25)
SelectB.configure(state='disabled',relief='sunken')
SelectB.configure(bg="gray25",fg="white")

for filename in glob.glob(filepath):
	a,b = str(filename).split("/")
	c,d = b.split(".")
	z = ""
	for l in range(12,len(c)):
		z = z + c[l]
	names.append(z)


	imgn[element] = PIL.Image.open(filename)
	imgn[element] = imgn[element].resize((40,40),PIL.Image.ANTIALIAS)
	imagen[element] = ImageTk.PhotoImage(imgn[element],master=root)
	row = int(element/14)
	column = element - row*14
	icons[element] = cv.create_image(300+70*column,800+70*row,image=imagen[element],anchor="nw")
	cv.tag_bind(icons[element],"<Button-1>",owo)
	if len(z) > 8:
		f = "calibri 8 bold"
	else:
		f="calibri 9 bold"
	nametags[element] = cv.create_text(320+70*column,850+70*row,text=z.upper(),anchor="center",fill="white",font=f)
	element = element + 1




root.mainloop()
