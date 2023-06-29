#this will be the personality quiz part of my program



from tkinter import*

 
from tkinter import messagebox as mb

window = Tk()

window.title("Giftlab")
window.geometry("500x500")


window.rowconfigure(0, weight = 1)
window.columnconfigure(0,weight = 1)


#creating different frames
picker = Frame(window) #this will pick who the gift is for, as it will change the results
quiz = Frame(window) #this will be the quiz 

for frame in (picker, quiz):
    frame.grid(row = 0, column = 0, sticky = "nsew")


def show_frame(frame):
    frame.tkraise()



show_frame(picker)

#creating the window frame picker:
#================= Picker Frame ================
#setting the font and backgrounds

font_header = ("Courier", 30)
bg_header = "#BEE3BA"
bg_other = "#DDF2D1"
font_other = ("Garamond", 22)

picker.configure(bg = bg_other)

titlelabel = Label(picker, text = "GIFTLAB", font = font_header, bg = bg_header)
titlelabel.place(x=200,y=10)


friends_btn = Button(picker, text = "Friends", font = font_other, highlightbackground = bg_header, command = lambda: show_frame(quiz))
friends_btn.place(x=50, y =50)

parents_btn = Button(picker, text = "Parents", font = font_other, highlightbackground = bg_header, command = lambda: show_frame(quiz))
parents_btn.place(x=50, y=100)

quitbtn = Button(picker, text = "Quit", font = font_other, highlightbackground = bg_header, command = window.destroy)
quitbtn.place(x=250, y=450)

#creating the questions and answers lists

#this personality quiz will have three options (a, b, c)
#i will use radio buttons to achieve this
#i am going to create 3 sets of questions







