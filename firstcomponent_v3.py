#this is my third version for my first component
#in this version, I will be focusing on making the UI look nicer. 

from tkinter import*

from tkinter import messagebox #importing messagebox to indicate code is working properly
window = Tk() #creating the window for the GUI 

window.title("Giftlab") #setting the title for the GUI app 
window.geometry("500x500") #setting the size of the window for the GUI App


#creating the function to check the name and age entry box:

def check_name():
    name = name_ent.get()
    while len(name) >= 1:
        if all(letter.isalpha() or letter.isspace() for letter in name):
            name_warning.config(text= "")
            return True
            break

        else:
            name_warning.config(text = "Invalid name. Please enter using only letters")
            name_ent.delete(0,END)
            return False

    else:
        len(name) <1
        name_warning.config(text = "Please enter your name: ")

        return False


    


def check_age():
    
    try:
        while len(age) >= 1:
            if int(age) >= 14 and int(age) <= 18:
                age_warning.config(text = "")
                return True
            else:
                age_warning.config(text = "Sorry! You must be aged between 14 to 18 years old!")
                age_ent.delete(0, END)
                return False
        else:
            len(age) < 1
            age_warning.config(text = "Please enter your age")
            return False
        
    except ValueError:
        age_warning.config(text = "Invalid Age. Please enter numerical value")
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



#creating labels and entry boxes

titlelabel = Label(window, text = "Giftlab", font = ("Courier",22))
titlelabel.place(x=10,y=10)

namelabel = Label(window, text = "Please enter your name: ", font = ("Arial", 22)) #this is the label which tells the user to enter their name
namelabel.place(x = 50, y = 50)

name_ent = Entry(window) #this is the entry box where the user will be able to enter their name 
name_ent.place()


agelabel = Label(window, text = "Please enter your age: ") #this is the label which tells the user to enter their age 
agelabel.place()


age_ent = Entry(window) #this is the entry box where the user will be able to enter their age
age_ent.place()

name_warning = Label(window, text = "")
name_warning.place()

age_warning = Label(window, text = "")
age_warning.place()

#creating buttons

quitbtn = Button(window, text = "Quit", command = window.destroy) #root.destroy means the program will close
quitbtn.place()


findgift_btn = Button(window, text = "Find A Gift!", command = check_entry)
findgift_btn.place()



window.mainloop() #this makes sure that the window is created
