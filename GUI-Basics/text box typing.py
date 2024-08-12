#2 Text box
from tkinter import *
window = Tk()
Label = Label(window, text="hello ayush!", font=('Arial', 18,'bold'),fg='#00ff00')
Label.place(x=0, y=0) # to the left of the window




#4 to add buttons of backspace,delete,submit
from tkinter import *

def submit():
    username = entry.get()
    print("hello "+ username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window,
              font=("arial", 40))
entry.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command = delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()

