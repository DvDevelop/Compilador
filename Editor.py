from tkinter import *
import tkinter as tk
from tkinter import filedialog
def new_file():
    text.delete(0.0,END)
    #need textbox
def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data)
    #need textbox
def save_file():
    filename="Untitled.txt"#get the current namefile and get the path
    data = text.get(0.0,END)
    file1=open(filename,"w")
    file1.write(data)
def save_as():
    file1 = filedialog.asksaveasfile(mode ='w') #return and save the current namefile and it's path
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
cursor_pos = text.index(tk.INSERT)
mensaje.set('Bienvenido a tu editor')
monitor = Label(gui, textvar=mensaje, justify='right')
monitor.pack(side='right')
gui.config(menu = mymenu)
print(cursor_pos)
gui.mainloop()


