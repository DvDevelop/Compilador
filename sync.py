import tkinter as tk
from tkinter import ttk


class DoubleScrollbarFrame(ttk.Frame):

    def __init__(self, master, **kwargs):

        ttk.Frame.__init__(self,  master, **kwargs)

        self.hscrollbar = ttk.Scrollbar(self, orient = tk.HORIZONTAL)
        self.vscrollbar = ttk.Scrollbar(self, orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        self.txt = tk.Text(self, bd=0, highlightthickness=0, 
                                                        yscrollcommand = self.vscrollbar.set,
                                                        xscrollcommand = self.hscrollbar.set)
        self.vscrollbar.config(command = self.txt.yview)
        self.hscrollbar.config(command = self.txt.xview)

    def pack(self, **kwargs):
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y,  expand=tk.FALSE)
        self.sizegrip.pack(in_ = self.hscrollbar, side = tk.BOTTOM, anchor = "se")
        self.txt.pack(side=tk.LEFT, padx=5, pady=5,fill=tk.BOTH, expand=tk.TRUE)

        ttk.Frame.pack(self, **kwargs)

    def get_frame(self):
        return self.txt


if __name__ == '__main__':
    root = tk.Tk()
    root.title( "Double scrollbar with tkinter" )
    root.minsize(width = 600, height = 600)
    frame = DoubleScrollbarFrame(root, relief="sunken")
    subframe = ttk.Frame( frame.get_frame() ) 
    txt = ttk.Label(subframe, text="Add things here !")
    txt.pack(anchor = 'center', fill = tk.Y, expand = tk.Y)
    subframe.pack(padx  = 15, pady   = 15, fill = tk.BOTH, expand = tk.TRUE)
    frame.pack( padx   = 5, pady   = 5, expand = True, fill = tk.BOTH)
