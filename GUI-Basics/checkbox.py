#5  checkbox
from tkinter import *

def display():
    if(x.get()==1):
        print("you agreed")
    else:
        print("you not agreed:(")

window = Tk()
x =IntVar()
check_button = Checkbutton(window,
                           text="i agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)
check_button.pack() 
window.mainloop()
