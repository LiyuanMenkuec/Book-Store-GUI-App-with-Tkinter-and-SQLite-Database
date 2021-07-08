"""
A program that stores this book information
"""

from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    try:
        global selected_row
        index=list1.curselection()[0]
        selected_row=list1.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selected_row[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_row[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_row[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_row[4])
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())



window=Tk()
window.wm_title("BookStore")

lable1=Label(window, text="Title")
lable1.grid(row=0,column=0)

lable2=Label(window, text="Author")
lable2.grid(row=0,column=2)


lable3=Label(window, text="Year")
lable3.grid(row=1,column=0)


lable4=Label(window, text="ISBN")
lable4.grid(row=1,column=2)


title_text=StringVar()
entry1=Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

author_text=StringVar()
entry2=Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

year_text=StringVar()
entry3=Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text=StringVar()
entry4=Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
scrollbar1=Scrollbar(window)
scrollbar1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=scrollbar1)
scrollbar1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

botton1=Button(window,text="View all",width=12,command=view_command)
botton1.grid(row=2,column=3)

botton2=Button(window,text="Search entry",width=12,command=search_command)
botton2.grid(row=3,column=3)

botton3=Button(window,text="Add entry",width=12,command=add_command)
botton3.grid(row=4,column=3)

botton4=Button(window,text="Update selected",width=12,command=update_command)
botton4.grid(row=5,column=3)

botton5=Button(window,text="Delete selected",width=12,command=delete_command)
botton5.grid(row=6,column=3)

botton6=Button(window,text="Close",width=12,command=window.destroy)
botton6.grid(row=7,column=3)

window.mainloop()


