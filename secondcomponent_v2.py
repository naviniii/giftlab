#this will be the personality quiz part of my program
#in this second version, I will be focusing on the quiz component. 


from tkinter import*
 
from tkinter import messagebox as mb




window = Tk()

window.title("Giftlab")
window.geometry("500x500")


window.rowconfigure(0, weight = 1)
window.columnconfigure(0,weight = 1)


friends_pic = PhotoImage(file = "friends.png", width = 150, height = 150)
parents_pic = PhotoImage(file = "parents.png", width = 150, height = 150)

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

font_header = ("Courier", 30) #stores the font for the heading 
bg_header = "#BEE3BA" #stores the background for the heading
bg_other = "#DDF2D1" #stores the background for other components 
font_other = ("Garamond", 22) #stores the font for other components 

picker.configure(bg = bg_other)

titlelabel = Label(picker, text = "GIFTLAB", font = font_header, bg = bg_header)
titlelabel.place(x=190,y=10)

wholabel = Label(picker, text = "Who is this gift for? \n Will it be for a parent, or a friend?", font = font_other, bg = bg_other)
wholabel.place(x = 100, y=75)


#creating the buttons
friends_btn = Button(picker, text = "Friends", bg = bg_other, image = friends_pic, compound = TOP, font = font_other, highlightbackground = bg_header, command = lambda: show_frame(quiz))
friends_btn.place(x=45, y =175)

parents_btn = Button(picker, text = "Parents", image = parents_pic, compound = TOP, font = font_other, highlightbackground = bg_header, command = lambda: show_frame(quiz))
parents_btn.place(x=300, y=175)

quitbtn = Button(picker, text = "Quit", font = font_other, highlightbackground = bg_header, command = window.destroy)
quitbtn.place(x=220, y=450)




#creating the questions and answers lists

#this personality quiz will have three options (a, b, c)
#i will use radio buttons to achieve this
#i am going to create 2 sets of questions







