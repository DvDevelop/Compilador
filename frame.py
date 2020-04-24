import os
import tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import  scrolledtext as st
from time import sleep
import subprocess

    
class initpage:
    #Constructor
    def __init__(self, parent):
        self.myparent = parent
        self.currentfile = "untitle"
        self.currentdir = "none"
        self.aux =0
        
        #menubar
        self.menu = tkinter.Menu()
        self.file = tkinter.Menu(tearoff=0)
        self.file.add_command(label =  "New file",command = self.new_file)
        self.file.add_command(label =  "Open file",command = self.open_file)
        self.file.add_command(label =  "Save file",command = self.save_file)
        self.file.add_command(label =  "Save file as",command = self.save_as)
        self.file.add_command(label =  "Exit",command = parent.destroy)
        self.menu.add_cascade(label="file",menu=self.file)
        self.cd = tkinter.Menu(tearoff=0)
        self.cd.add_command(label = "lexico", command = self.hacer_click ) #,command = subprocess.call(["python", "script.py","Hola"]) 
        self.cd.add_command(label = "sintactico")
        self.cd.add_command(label = "semantico")
        self.cd.add_command(label = "compilar")
        self.menu.add_cascade(label="compile and Debug", menu = self.cd)
        parent.config(menu = self.menu)

        #frame botones acceso directo
        self.bar = tkinter.Frame(parent)
        self.bar.pack(side=tkinter.TOP,fill="both",expand=1)
        self.bar.config(height=15)
        dirname = os.path.dirname(__file__)
        imagedir = dirname + "\\icos\\Negro\\new.png"
        self.photo1 = tkinter.PhotoImage(file = imagedir)
        self.btnnew = tkinter.Button(self.bar,command = self.new_file)
        self.btnnew.pack(side= tkinter.LEFT)
        self.btnnew.config(image = self.photo1 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\open.png"
        self.photo2 = tkinter.PhotoImage(file = imagedir)
        self.btnopen = tkinter.Button(self.bar,command = self.open_file)
        self.btnopen.pack(side= tkinter.LEFT)
        self.btnopen.config(image = self.photo2 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\save.png"
        self.photo3 = tkinter.PhotoImage(file = imagedir)
        self.btnsave = tkinter.Button(self.bar,command = self.save_file)
        self.btnsave.pack(side= tkinter.LEFT)
        self.btnsave.config(image = self.photo3 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\guardar.png"
        self.photo8 = tkinter.PhotoImage(file = imagedir)
        self.btnsaveas = tkinter.Button(self.bar,command = self.save_as)
        self.btnsaveas.pack(side= tkinter.LEFT)
        self.btnsaveas.config(image = self.photo8 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\exit.png"
        self.photo9 = tkinter.PhotoImage(file = imagedir)
        self.btnsaveas = tkinter.Button(self.bar,command = parent.destroy)
        self.btnsaveas.pack(side= tkinter.LEFT)
        self.btnsaveas.config(image = self.photo9 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\lexico.png"
        self.photo4 = tkinter.PhotoImage(file = imagedir)
        self.btnsave = tkinter.Button(self.bar, command = self.hacer_click)
        self.btnsave.pack(side= tkinter.LEFT)
        self.btnsave.config(image = self.photo4 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\sintactico.png"
        self.photo5 = tkinter.PhotoImage(file = imagedir)
        self.btnsave = tkinter.Button(self.bar)
        self.btnsave.pack(side= tkinter.LEFT)
        self.btnsave.config(image = self.photo5 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\semantico.png"
        self.photo6 = tkinter.PhotoImage(file = imagedir)
        self.btnsave = tkinter.Button(self.bar)
        self.btnsave.pack(side= tkinter.LEFT)
        self.btnsave.config(image = self.photo6 , compound = tkinter.LEFT)
        imagedir = dirname + "\\icos\\Negro\\compilar.png"
        self.photo7 = tkinter.PhotoImage(file = imagedir)
        self.btnsave = tkinter.Button(self.bar)
        self.btnsave.pack(side= tkinter.LEFT)
        self.btnsave.config(image = self.photo7 , compound = tkinter.LEFT)
        #frame de codigo
        self.div = tkinter.Frame(parent)
        self.div.pack(side=tkinter.TOP,fill='both',expand=1)
        self.div.config(width=600, height=300)
        
        self.txt = tkinter.Text(self.div,width=3, height=25)
        self.txt.pack(side=tkinter.LEFT)
        self.txt.config(state= tkinter.DISABLED)
        self.txt2 = tkinter.Text(self.div,width=80, height=25,wrap=tkinter.NONE)
        self.txt2.pack(side=tkinter.LEFT)
        bindtags = list(self.txt2.bindtags())
        bindtags.insert(2, "custom")
        self.txt2.bindtags(tuple(bindtags))
        self.txt2.bind_class("custom", "<Key>", lambda event, arg=self: self.getLC(event))
        self.scrollb = tkinter.Scrollbar(self.div,command=self.y_view)
        self.scrollh = tkinter.Scrollbar(self.myparent,orient = tkinter.HORIZONTAL,command=self.x_view)
        self.scrollb.pack(side=tkinter.LEFT,fill=tkinter.Y)
        self.scrollh.pack(fill=tkinter.X)
        self.txt2['xscrollcommand'] = self.scrollh.set
        self.txt.config(yscrollcommand=self.updatescroll)
        self.txt2.config(yscrollcommand=self.updatescroll)
##        self.txt2['yscrollcommand'] = self.scrollb.set
        
        #Abrir archivos para imprimir frame derecho (tokens)
        #archivo_token=open("token.txt","r")
        #linesfilelist = archivo_token.readlines()
        #frame derecho
        self.divmr = tkinter.Frame(self.div)
        self.divmr.pack(fill=tkinter.BOTH)
        self.divmr.config(width=500, height=300)
        #tabs derecho
        self.tabsr = ttk.Notebook(self.divmr)
        #tab1
        self.f1intab1 = tkinter.Frame(self.tabsr)
        self.f1ttab1 = st.ScrolledText(self.f1intab1)

        #self.f1intab1 = ttk.Label(self.tabsr, text = linesfilelist)
        #archivo_token.close()
        
        self.f1ttab1.config(state= tkinter.DISABLED)
        self.f1ttab1.pack()
        #tab2
        self.f2intab1 = tkinter.Frame(self.tabsr)
        self.f1ttab2 = st.ScrolledText(self.f2intab1)
        self.f1ttab2.config(state= tkinter.DISABLED)
        self.f1ttab2.pack()
        #tab3
        self.f3intab1 = tkinter.Frame(self.tabsr)
        self.f1ttab3 = st.ScrolledText(self.f3intab1)
        self.f1ttab3.config(state= tkinter.DISABLED)
        self.f1ttab3.pack()
        #tab4
        self.f4intab1 = tkinter.Frame(self.tabsr)
        self.f1ttab4 = st.ScrolledText(self.f4intab1)
        self.f1ttab4.config(state= tkinter.DISABLED)
        self.f1ttab4.pack()
        #tab5
        self.f5intab1 = tkinter.Frame(self.tabsr)
        self.f1ttab5 = st.ScrolledText(self.f5intab1)
        self.f1ttab5.config(state= tkinter.DISABLED)
        self.f1ttab5.pack()

       # self.lex_label = ttk.Label(self.tabsr, text = linesfilelist)
 
        self.tabsr.add(self.f1intab1, text='Lexico')   
        self.tabsr.add(self.f2intab1, text='Sintactico')
        self.tabsr.add(self.f3intab1, text='Semantico')
        self.tabsr.add(self.f4intab1, text='Hash Table')
        self.tabsr.add(self.f5intab1, text='Codigo intermedio')
        self.tabsr.pack()
        
        #Abrir archivos para imprimir frame abajo (errores)
        archivo_error=open("errores.txt","r")
        linesfileliste = archivo_error.readlines()
        #frame bajo
        self.divmb =tkinter.Frame(parent)
        self.divmb.pack()
        self.divmb.config(height=100)
        #tabs bajo
        self.tabsb = ttk.Notebook(self.divmb)
        #tab1
        self.f1intab2 = tkinter.Frame(self.tabsb)
        self.f2ttab1 = st.ScrolledText(self.f1intab2)

        #self.f1intab2 = ttk.Label(self.tabsb, text = linesfileliste)  
        #archivo_error.close()
        
        self.f2ttab1.config(width=170, height=10)
        self.f2ttab1.config(state= tkinter.DISABLED)
        self.f2ttab1.pack()
        #tab2
        self.f2intab2 = tkinter.Frame(self.tabsb)
        self.f2ttab2 = st.ScrolledText(self.f2intab2)
        self.f2ttab2.pack()
        self.f2ttab2.config(width=170, height=10)
        self.f2ttab2.config(state= tkinter.DISABLED)
        self.f2ttab2.pack()
        #tab3
        self.f3intab2 = tkinter.Frame(self.tabsb)
        self.f2ttab3 = st.ScrolledText(self.f3intab2)
        self.f2ttab3.pack()
        self.f2ttab3.config(width=170, height=10)
        self.f2ttab3.config(state= tkinter.DISABLED)
        self.f2ttab3.pack()
        #tab4
        self.f4intab2 = tkinter.Frame(self.tabsb)
        self.f2ttab4 = st.ScrolledText(self.f4intab2)
        self.f2ttab4.pack()
        self.f2ttab4.config(width=170, height=10)
        self.f2ttab4.config(state= tkinter.DISABLED)
        self.f2ttab4.pack()
        self.tabsb.add(self.f1intab2, text='Errores Lexicos')
        self.tabsb.add(self.f2intab2, text='Errores Sintacticos')
        self.tabsb.add(self.f3intab2, text='Errores Semanticos')
        self.tabsb.add(self.f4intab2, text='Resultados')
        self.tabsb.pack(side=tkinter.LEFT)
        
        #frame fondo
        self.div2 = tkinter.Frame(parent)
        self.div2.pack(side=tkinter.BOTTOM,fill='both',expand=1)
        #mensajes 
        self.mensaje = tkinter.StringVar()
        self.mensaje.set('linea y columna')
        self.monitor = tkinter.Label(self.div2, textvar=self.mensaje, justify='right')
        self.monitor.pack(side='right')

        self.mensaje2 = tkinter.StringVar()
        self.mensaje2.set(self.currentfile)
        self.monitor2 = tkinter.Label(self.div2, textvar=self.mensaje2, justify='left')
        self.monitor2.pack(side='left')

    def new_file(self):
        res = messagebox.askquestion('Alert','Quiere guardar el archivo actual')
        if (res == "yes"):
            print("quiere guardarlo")
            self.save_as()
        else:
            self.txt2.delete(0.0,tkinter.END)
            self.currentfile = "untitle"
            self.mensaje2.set(self.currentfile)
            self.myparent.update_idletasks()
    def  open_file(self):
        res = messagebox.askquestion('Alert','Quiere guardar el archivo actual')
        if (res == "yes"):
            print("quiere guardarlo")
            self.save_as()
        else:
            file1 = filedialog.askopenfile(mode='r')
            if (file1 is not None):
                self.currentfile = os.path.basename(file1.name)
                self.currentdir = os.path.dirname(file1.name)
                data = file1.read()
                self.txt2.delete(0.0,tkinter.END)
                self.txt2.insert(0.0,data)
                self.mensaje2.set(self.currentfile)
                self.myparent.update_idletasks()
                self.actualizar()
    def save_file(self):
        if(self.currentdir == "none"):
            self.save_as()
        else:
            filedir = os.path.join(self.currentdir, self.currentfile)
            data = self.txt2.get(0.0,tkinter.END)
            file = open(filedir,"w")
            file.write(data)
    def save_as(self):
        file = file1 = filedialog.asksaveasfile(mode ='w') #return and save the current namefile and it's path
        self.currentfile = os.path.basename(file1.name)
        self.currentdir = os.path.dirname(file1.name)
        data = self.txt2.get(0.0,tkinter.END)
        file.write(data)
        self.mensaje2.set(self.currentfile)
        self.myparent.update_idletasks()
    def getLC(*args):
        event = args[1]
        self = args[0]
        total = int(self.txt2.index('end-1c').split('.')[0])
        if (self.aux != total):
            self.aux = total
            self.txt.config(state= "normal")
            self.txt.delete(0.0,tkinter.END)
            for i in range(1,total+1):
                self.txt.insert('end', str(i) +"\n")
            self.txt.config(state= tkinter.DISABLED)
        (line,c) = map(int,event.widget.index(tkinter.INSERT).split("."))
        self.mensaje.set("ln:"+str(line)+"  Col:"+str(c))
        self.myparent.update_idletasks()
    def y_view(self,*args):
        self.txt.yview_moveto(args[1])
        self.txt2.yview_moveto(args[1])
    def x_view(self,*args):
        self.txt2.xview(*args)
    def updatescroll(self, first, last, type=None):
        self.txt.yview_moveto(first)
        self.txt2.yview_moveto(float(first))
        self.scrollb.set(first,last)
    def actualizar(self):
        self.txt.config(state= "normal")
        total = int(self.txt2.index('end-1c').split('.')[0])
        for i in range(1,total+1):
                self.txt.insert('end', str(i) +"\n")
        self.txt.config(state= tkinter.DISABLED)
    def getlexico(self):
        with open("token.txt", 'r') as file:
            data = file.read()
        with open("errores.txt","r") as file:
            dataE = file.read()
        self.f1ttab1.config(state= "normal")
        self.f1ttab1.delete("1.0",tkinter.END)
        self.f1ttab1.insert("1.0",data)
        self.f1ttab1.config(state= tkinter.DISABLED)
        self.f2ttab1.config(state = "normal")
        self.f2ttab1.delete("1.0",tkinter.END)
        self.f2ttab1.insert("1.0",dataE)
        self.f2ttab1.config(state= tkinter.DISABLED)
    def hacer_click(self):
        #print("funciona")
        self.save_file()
        filedir = os.path.join(self.currentdir, self.currentfile)
        
        info = subprocess.call(["python", "lexico.py",filedir])  #,"Hola"
        self.getlexico()
    
#main 
main_window = tkinter.Tk()
wdn=  initpage(main_window)
main_window.mainloop()

