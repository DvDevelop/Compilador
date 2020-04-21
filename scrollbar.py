import tkinter
import tkinter.ttk as ttk

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tkinter.Text(self,width=50, height=10)
        self.txt2 = tkinter.Text(self,width=50, height=10)
        self.txt.grid(row=0, column=0, padx=2, pady=2)
        self.txt2.grid(row=0, column=1, padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.multiple_yview)
        scrollb.grid(row=0, column=2,ipady=60)
        self.txt2['yscrollcommand'] = scrollb.set

    def multiple_yview(self,*args):
        self.txt.yview(*args)
        self.txt2.yview(*args)
        
main_window = tkinter.Tk()

combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True)
combo.config(width=500, height=300)


style = ttk.Style()
style.theme_use('clam')

main_window.mainloop()
