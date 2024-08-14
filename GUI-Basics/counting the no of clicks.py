#3 counting the no of clicks
from tkinter import *
count = 0  # this will count the number of clicks 

def click():
    global count
    count+=1
    print(count)

window = Tk()

window.geometry("500x500")
button = Button(window,    #button created
                text="click me!",
                command=click,
                font=("comiic sans", 20))
button.pack()

window.mainloop()
