from tkinter import *
from tkinter import messagebox as MessageBox
import tkinter

search_list = list()
s = ""

def reset_list():
    if s != entry_widget_name.get():
        print(entry_widget_name.get())
        search_list.clear()
        text_widget_name.tag_remove(SEL, 1.0,"end-1c")

def search_words():
    global search_list
    global s
    text_widget_name.focus_set()
    s = entry_widget_name.get()
    x = 10
    print(s)
    while x>0:
        if s:
            if search_list == []:
                idx = "1.0"
            else:
                idx = search_list[-1]
            idw =  text_widget_name.search("/", idx, nocase=1, stopindex=END)
            idx = text_widget_name.search(s, idx, nocase=1, stopindex=END)
            print(idx)
            lastidx = '%s+%dc' % (idx, len(s))
            """try:
                text_widget_name.tag_remove(SEL, 1.0,lastidx)
            except:
                pass"""

            try:

                text_widget_name.tag_add("N", idw, idx + "lineend")
                text_widget_name.tag_add("C", idx, idx + "lineend")
                print(text_widget_name.get(idx,idx +" lineend+1c"))
                counter_list = []
                counter_list = str(idx).split('.')      
                search_list.append(lastidx)
            except:
                search_list.clear()
                text_widget_name.tag_remove(SEL, 1.0,"end-1c")
                break
root = Tk()
root.geometry("540x460")
lbl_frame_entry = LabelFrame(root, text="Enter the text to search", padx=5, pady=5)
lbl_frame_entry.pack(padx=10, pady=5, fill="both")

entry_widget_name = Entry(lbl_frame_entry, width=50, justify = "left")
entry_widget_name.pack(fill="both")

lbl_frame_text = LabelFrame(root, text="Enter the text here", padx=5, pady=5, height=260)
lbl_frame_text.pack(padx=10, pady=5, fill="both", expand=True)

text_widget_name = Text(lbl_frame_text)
text_widget_name.tag_configure("N", foreground="Red")
text_widget_name.tag_configure("C", foreground="gray")

text_widget_name.pack(fill="both", expand=True)

scrollbar = Scrollbar(text_widget_name, orient="vertical", command=text_widget_name.yview, cursor="arrow")
scrollbar.pack(fill="y", side="right")
text_widget_name.config(yscrollcommand=scrollbar.set)

button_name = Button(root, text="Search", command=search_words, padx=5, pady=5)
button_name.pack()
root.mainloop()
