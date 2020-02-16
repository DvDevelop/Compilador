from tkinter import *
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
gui.geometry("1000x1000")
text = Text(gui, bg= "#252525", fg="#FFFFFF",width="170",heigh="170",insertbackground='white')
text .pack()
mymenu = Menu()
list1= Menu()
list1.add_command(label = 'New file',command = new_file)
list1.add_command(label = 'Open file',command = open_file)
list1.add_command(label = 'Save file',command = save_file)
list1.add_command(label = 'Save file as',command = save_as)
list1.add_command(label = 'Exit',command = gui.destroy)
mymenu.add_cascade(label='File',menu=list1)
gui.config(menu = mymenu)
gui.mainloop()
