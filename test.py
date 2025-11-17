from tkinter import *
def printing():
    print(e.get())
window=Tk()
window.geometry("300x300")
window.resizable(True,False)
e=Entry(window,width=30)
e.pack()
bt=Button(window,text="click me",command=printing)
bt.pack()
window.mainloop()