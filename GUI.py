from tkinter import *
from tkinter import messagebox as mb

ask = ["كلب", "قطه", "اسد", "نمر", "زرافه", "فيل", "تمساح", "ارنب", "العصفور", "ببغاء"]
answer = ["dog", "cat", "lion", "tiger", "giraffe", "elephant", "crocodile", "rabbit", "sparrow", "parrot"]

size = len(ask)
index = 0
numhints = 0

def thend():
    new_window = Toplevel(width=400, height=300)
    new_window.resizable(False, False)
    
    bg_image1 = PhotoImage(file='backgrond.PNG')
    bg_label1 = Label(new_window, image=bg_image1)
    bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
    new_window.bg_image1 = bg_image1  

    lb_message = Label(new_window, text="YOU FINISHED YOUR WORDS TODAY!", font=1, fg="black")
    lb_message.place(x=50, y=150)
    lb_message1 = Label(new_window, text="CORRECT ANSWERS", font=15, fg="black")
    lb_message1.place(x=50, y=40)
    lb_message2 = Label(new_window, text="WRONG ANSWERS", font=15, fg="black")
    lb_message2.place(x=50, y=100)
    correct = Label(new_window, text=lb_score1["text"], font=10, width=3,fg="black")
    correct.place(x=230, y=40)
    wrong = Label(new_window, text=lb_score2["text"], font=10, width=3, fg="black")
    wrong.place(x=230, y=100)

    lb_score1.config(text='0')
    lb_score2.config(text='0')

    
    bt_exit = Button(new_window, text="Exit", font=15, command=new_window.destroy)
    bt_exit.place(x=150, y=200)

    new_window.bind("<Escape>", lambda event: new_window.destroy())


def click():
    global numhints, index
    
    if en.get() == str(answer[index]):  # correct input
        index += 1
        if index == size: thend()
        index %= size
        lb_score1.config(text=str(int(lb_score1["text"]) + 1))
        lb_arabic1.config(text=str(ask[index]))
        numhints = 0
        en.delete(0, END)
        lb_hint.config(text="")
    
    elif en.get() == "":  # empty input
        mb.showerror("An Error", "You should enter a word")
    else:  # incorrect 
        lb_score2.config(text=str(int(lb_score2["text"]) + 1))
        en.delete(0, END)

def click_next():
    global index, size
    index += 1
    if index == size: thend()
    index %= size
    lb_arabic1.config(text=str(ask[index]))
    en.delete(0, END)
    lb_hint.config(text="")

def click_back():
    global index
    if index: index -= 1
    lb_arabic1.config(text=str(ask[index]))
    en.delete(0, END)
    lb_hint.config(text="")

def hintclick():
    global numhints, index
    numhints += 1
    ans = ''
    word = str(answer[index])    
    for i in range(len(word)):
        if i < numhints:
            ans += word[i]
        else:
            ans += '?'
    lb_hint.config(text=ans)

Window = Tk()
Window.title("Flashcard app")
Window.geometry("500x400")
Window.resizable(False, False)

bg_image = PhotoImage(file='backgrond.PNG')
bg_label = Label(Window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

bg_color = "white"  
lb_score = Label(Window, text="Successful attempts:", font=20, bg=bg_color, fg="black")
lb_score.place(x=20, y=30)
lb_score1 = Label(Window, text="0", font=10, width=3, bg=bg_color, fg="black")
lb_score1.place(x=190, y=30)

lb_score = Label(Window, text="Failed attempts:", font=20, bg=bg_color, fg="black")
lb_score.place(x=300, y=30)
lb_score2 = Label(Window, text="0", font=10, width=3, bg=bg_color, fg="black")
lb_score2.place(x=440, y=30)

lb_arabic = Label(Window, text="The word:", font=25, bg=bg_color, fg="black")
lb_arabic.place(x=20, y=80)

lb_arabic1 = Label(Window, width=8, text=str(ask[index]), font=20, bg=bg_color, fg="black")
lb_arabic1.place(x=260, y=80)

lb_enter = Label(Window, text="Enter meaning:", font=25, bg=bg_color, fg="black")
lb_enter.place(x=20, y=125)
en = Entry(Window, font=20)
en.place(x=200, y=125, height=30, width=200)

lb_hint_mass = Label(Window, text="Hint:", font=25, bg=bg_color, fg="black")
lb_hint_mass.place(x=20, y=170)
lb_hint = Label(Window, text=" ", font=25, bg=bg_color, fg="black")
lb_hint.place(x=260, y=170)


bt_hint = Button(Window, text="Hint", activebackground="green", font=15, bd=4, command=hintclick)
bt_hint.place(x=50, y=250)

bt_enter = Button(Window, text="Enter", activebackground="red", font=15, bd=4, command=click)
bt_enter.place(x=170, y=250)  

bt_next = Button(Window, text="Next", activebackground="red", font=15, bd=4, command=click_next)
bt_next.place(x=420, y=250)

bt_back = Button(Window, text="Back", activebackground="red", font=15, bd=4, command=click_back)
bt_back.place(x=300, y=250)

Window.bind('<Return>', lambda event: click())  
Window.bind('<Right>', lambda event: click_next())  
Window.bind('<Left>', lambda event: click_back())

Window.mainloop()