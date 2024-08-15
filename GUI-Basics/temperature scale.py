
#6 temperature scale
from tkinter import *
def submit():
    print("the temperature is "+ str(scale.get())+"degree C")

window = Tk()

scale = Scale(window,from_= 0, to = 100)
scale.pack()
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()
