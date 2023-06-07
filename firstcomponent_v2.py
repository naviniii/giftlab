#this is my second version for my first component
#in this version, I will be focusing on creating the buttons so that the entry of the name and age can be checked


from tkinter import*

from tkinter import messagebox #importing messagebox to indicate code is working properly
window = Tk() #creating the window for the GUI 

window.title("Giftlab") #setting the title for the GUI app 
window.geometry("500x500") #setting the size of the window for the GUI App



#creating the function to check the name and age entry box:

def check_entry():
    name = name_ent.get()
    age = age_ent.get()

    if len(name) < 1:
        name_warning.config(text = "Please enter a name")
    if len(name) >= 1:
        name_warning.config(text = "") 

    if len(age)< 1:
        age_warning.config(text = "Please enter an age")
    if len(age) >= 1:
        age_warning.config(text = "") 
#this will give a message on the app screen for the user to enter their name and/or age
        
    #to make sure that the name entry box only contains alpha letters:

    while len(name)>= 1:
        if all(name.isalpha() or name.isspace() for entry in name):

            name_warning.config(text = "")
            return True
        
        break
        

    else:
        name_warning.config(text = "Please enter a name containing only letters")
        


#creating labels and entry boxes


namelabel = Label(window, text = "Please enter your name: ") #this is the label which tells the user to enter their name
namelabel.pack()
#I will use the pack method for my first version
#However, I will find a better layout manager later on in my code
#this is to make sure that my program is aesthetically pleasing, and in the correct order 


name_ent = Entry(window) #this is the entry box where the user will be able to enter their name 
name_ent.pack()


agelabel = Label(window, text = "Please enter your age: ") #this is the label which tells the user to enter their age 
agelabel.pack()


age_ent = Entry(window) #this is the entry box where the user will be able to enter their age
age_ent.pack()

name_warning = Label(window, text = "")
name_warning.pack()

age_warning = Label(window, text = "")
age_warning.pack()

#creating buttons

quitbtn = Button(window, text = "Quit", command = window.destroy) #root.destroy means the program will close
quitbtn.pack()


findgift_btn = Button(window, text = "Find A Gift!", command = check_entry)
findgift_btn.pack()



window.mainloop() #this makes sure that the window is created
