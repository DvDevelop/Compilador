from tkinter import *
search_list = list()
operators = ['+', '-', '*', '/', '<', '>', ':=', '==', '!=','>=', '<=']
forsearchW = (
        'main', 'if', 'then', 'else', 'end', 'do', 'while', 'repeat', 'until', 'cin', 'cout', 'real', 'int', 'boolean','+', '-', '*', '/', '<', '>', ':=', '==', '!=','>=', '<=','1','2','3','4','5','6','7','8','9','0',"//"
        )
def search_words():
    global search_list
    for word in forsearchW:
        while True:
            if word:
                if search_list == []:
                    idx = "1.0"
                else:
                    idx = search_list[-1]
                idx = text_widget_name.search(word, idx, stopindex=END)
                lastidx = '%s+%dc' % (idx, len(word))
                idxf ='%s+%dc' % (idx, len(word)+1)
                idxb ='%s-%dc' % (idx, 1)
                
            """try:
                   text_widget_name.tag_remove("N", 1.0,lastidx)
                   text_widget_name.tag_remove("RW", 1.0,lastidx)
            except:
                pass"""
            if idx:
                inf = text_widget_name.get(lastidx,idxf)
                inb = text_widget_name.get(idxb,idx)
                try:
                    if word == "//":
                        print("entro")
                        text_widget_name.tag_add("C", idx,  idx + "lineend")
                    elif word in operators:
                        text_widget_name.tag_add("O", idx, lastidx)
                    else:
                        if idx:
                            inf = text_widget_name.get(lastidx,idxf)
                            inb = text_widget_name.get(idxb,idx)
                            if (inf == " " and inb == " ") or (len(inb) == 0 or inf == chr(10)) or inb == chr(10):
                                if not word.isnumeric():
                                    text_widget_name.tag_add("RW", idx, lastidx)
                                if((inf.isalpha() or inb.isalpha()) or (inf == " " and inb == " ") or ((len(inb) == 0 or inf == chr(10)))or inb == chr(10)):
                                     if word.isnumeric():
                                        text_widget_name.tag_add("N", idx, lastidx)
                    counter_list = []
                    counter_list = str(idx).split('.')
                    search_list.append(lastidx)
                except:
                    search_list.clear()
                    break
            else:
                search_list.clear()
                break
    
    """while True:
        word = "//"
        if word:
            if search_list == []:
                idx = "1.0"
            else:
                idx = search_list[-1]
                
            idx = text_widget_name.search(word, idx, stopindex=END)
            
            try:
                text_widget_name.tag_remove("O",idx + "lineend")
                text_widget_name.tag_add("C", idx,  idx + "lineend")
                    
                counter_list = []
                counter_list = str(idx).split('.')
                (line,c) = map(int,idx.split("."))
                lastidx = str(line+1)+".0"
                print(lastidx)
                search_list.append(lastidx)
                print(search_list)
            except:
                search_list.clear()
                break
        else:
            search_list.clear()
            break"""
            
root = Tk()
root.geometry("540x460")

lbl_frame_entry = LabelFrame(root, text="Enter the text to search", padx=5, pady=5)
lbl_frame_entry.pack(padx=10, pady=5, fill="both")

entry_widget_name = Entry(lbl_frame_entry, width=50, justify = "left")
entry_widget_name.pack(fill="both")
lbl_frame_text = LabelFrame(root, text="Enter the text here", padx=5, pady=5, height=260)
lbl_frame_text.pack(padx=10, pady=5, fill="both", expand=True)
text_widget_name = Text(lbl_frame_text)
text_widget_name.tag_configure("RW", foreground="Blue")
text_widget_name.tag_configure("N", foreground="Red")
text_widget_name.tag_configure("C", foreground="gray")
text_widget_name.tag_configure("O", foreground="Green")
text_widget_name.pack(fill="both", expand=True)

scrollbar = Scrollbar(text_widget_name, orient="vertical", command=text_widget_name.yview, cursor="arrow")
scrollbar.pack(fill="y", side="right")
text_widget_name.config(yscrollcommand=scrollbar.set)

button_name = Button(root, text="Search", command=search_words, padx=5, pady=5)
button_name.pack()
root.mainloop()
