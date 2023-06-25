#this is my third version for my first component
#in this version, I will be focusing on making the UI look nicer. 

from tkinter import*

from tkinter import messagebox #importing messagebox to indicate code is working properly
window = Tk() #creating the window for the GUI 

window.title("Giftlab") #setting the title for the GUI app 
window.geometry("520x500") #setting the size of the window for the GUI App
window.config(bg = "#DDF2D1")


#creating the function to check the name and age entry box:

def check_name():
    name = name_ent.get()
    while len(name) >= 1:
        if all(letter.isalpha() or letter.isspace() for letter in name):
            name_warning.config(text= "")
            return True
            break

        else:
            name_warning.config(text = "Invalid name! Please enter using letters")
            name_ent.delete(0,END)
            return False

    else:
        len(name) <1
        name_warning.config(text = "Please enter your name ")

        return False


    


def check_age():
    
    try:
        while len(age) >= 1:
            if int(age) >= 14 and int(age) <= 18:
                age_warning.config(text = "")
                return True
            else:
                age_warning.config(text = "Sorry! You must be 14 to 18 years old!")
                age_ent.delete(0, END)
                return False
        else:
            len(age) < 1
            age_warning.config(text = "Please enter your age")
            return False
        
    except ValueError:
        age_warning.config(text = "Invalid Age! Please enter numerical value")
        age_ent.delete(0,END)
        return False
            


def check_entry():
    global name
    name = name_ent.get()
    global age
    age = age_ent.get()

    validate_name = check_name()
    validate_age = check_age()

    if validate_age == True and validate_name == True:
        print("Correct!")


#importing welcome message
welcome_file = open("welcome_message.txt", "r", encoding = "utf-8")
welcome = welcome_file.read()
welcome_file.close()

backgrounds = "#BEE3BA"

#creating labels and entry boxes

titlelabel = Label(window, text = "GIFTLAB", font = ("Courier",30), bg = backgrounds)
titlelabel.place(x=200,y=10)

sloganlabel = Label(window, text = "Give a gift they'll never forget!", font = ("Courier", 15, "italic"), bg = backgrounds)
sloganlabel.place(x = 100, y = 55)

welcomelabel = Label(window, text = welcome, font = ("Garamond", 15), bg = "#DDF2D1")
welcomelabel.place(x=10, y = 100)


                
namelabel = Label(window, text = "Please enter your name: ", font = ("Garamond", 22), bg = "#DDF2D1") #this is the label which tells the user to enter their name
namelabel.place(x=25, y=270)

name_ent = Entry(window) #this is the entry box where the user will be able to enter their name 
name_ent.place(x = 250, y = 270)


agelabel = Label(window, text = "Please enter your age: ", font = ("Garamond", 22), bg = "#DDF2D1") #this is the label which tells the user to enter their age 
agelabel.place(x=25, y = 340)


age_ent = Entry(window) #this is the entry box where the user will be able to enter their age
age_ent.place(x=250, y = 340)

name_warning = Label(window, text = "", font = ("Garamond", 15), bg = "#DDF2D1", fg = "red")
name_warning.place(x=250, y = 300)

age_warning = Label(window, text = "", font = ("Garamond", 15), bg = "#DDF2D1", fg = "red")
age_warning.place(x = 250, y = 370)

#creating buttons

quitbtn = Button(window, text = "Quit", command = window.destroy, highlightbackground = backgrounds, font = ("Garamond", 22)) #root.destroy means the program will close
quitbtn.place(x =350, y = 420)


findgift_btn = Button(window, text = "Find A Gift!", command = check_entry, highlightbackground = backgrounds, font = ("Garamond", 22))
findgift_btn.place(x = 170, y = 420)



window.mainloop() #this makes sure that the window is created
