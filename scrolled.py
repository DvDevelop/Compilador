import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
def countlines(event, arg):
    print(event)
    arg.scrolledtext2.yview_scroll(-1*(event.delta//120), "units")
    arg.scrolledtext1.yview_scroll(-1*(event.delta//120), "units")
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scrolledtext2=st.Text(self.ventana1, width=3, height=10)
        for i in range(1,20):
            self.scrolledtext2.insert('end', str(i) +"\n")
        self.scrolledtext2.config(state= tk.DISABLED)
        #self.scrolledtext2.config(state= "normal")
        self.scrolledtext2.pack(side = tk.LEFT)
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext1.pack(side = tk.LEFT)
        bindtags = list(self.scrolledtext1.bindtags())
        bindtags.insert(2, "custom")
        self.scrolledtext1.bindtags(tuple(bindtags))
        self.scrolledtext1.bind_class("custom", "<MouseWheel>", lambda event, arg=self: countlines(event, arg))
        #self.framecopia()
        mensaje = tk.StringVar()
        mensaje.set('Bienvenido a tu editor')
        monitor = tk.Label(self.ventana1, textvar=mensaje, justify='right')
        monitor.pack(fill='both',expand=1,side='right')
        self.ventana1.mainloop()


    def framecopia(self):
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Region")
        self.labelframe1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.label1=ttk.Label(self.labelframe1, text="Desde fila:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5, sticky="e")
        self.label2=ttk.Label(self.labelframe1, text="Desde columna:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5, sticky="e")

        self.label3=ttk.Label(self.labelframe1, text="Hasta fila:")
        self.label3.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5, sticky="e")
        self.label4=ttk.Label(self.labelframe1, text="Hasta columna:")
        self.label4.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.dato4=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe1, textvariable=self.dato4)
        self.entry4.grid(column=1, row=3, padx=5, pady=5, sticky="e")

        self.boton1=ttk.Button(self.labelframe1, text="Copiar", command=self.copiar)
        self.boton1.grid(column=1, row=4, padx=10, pady=10)


    def copiar(self):
        iniciofila=self.dato1.get()
        iniciocolumna=self.dato2.get()
        finfila=self.dato3.get()
        fincolumna=self.dato4.get()
        datos=self.scrolledtext1.get(iniciofila+"."+iniciocolumna, finfila+"."+fincolumna)
        self.scrolledtext2.delete("1.0", tk.END)        
        self.scrolledtext2.insert("1.0", datos)
        

aplicacion1=Aplicacion() 
