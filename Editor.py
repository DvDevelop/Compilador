from tkinter import *
import tkinter as tk
from tkinter import filedialog
def new_file():
    text.delete(0.0,END)
def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data)
def save_file():
    filename="Untitled.txt"
    data = text.get(0.0,END)
    file1=open(filename,"w")
    file1.write(data)
def save_as():
    file1 = filedialog.asksaveasfile(mode ='w')
    data = text.get(0.0,END)
    file.write(data)

gui = Tk()
gui.title('DvD')
gui.geometry("700x500")
text = Text(gui, bg= "#252525", fg="#FFFFFF",width="50",heigh="30",insertbackground='white')#170x170
scroll = Scrollbar(gui,orient="vertical", command=text.yview)
text.focus()
text.config(yscrollcommand= scroll.set)
text .pack(fill='both',expand=1)
mymenu = Menu()
list1= Menu(tearoff=0)
list1.add_command(label = 'New file',command = new_file)
list1.add_command(label = 'Open file',command = open_file)
list1.add_command(label = 'Save file',command = save_file)
list1.add_command(label = 'Save file as',command = save_as)
list1.add_command(label = 'Exit',command = gui.destroy)
mymenu.add_cascade(label='File',menu=list1)
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
print (tk.INSERT)
monitor = Label(gui, textvar=str(tk.INSERT), justify='right')
monitor.pack(side='left')
gui.config(menu = mymenu)
gui.mainloop()


