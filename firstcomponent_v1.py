
from tkinter import*

window = Tk() #creating the window for the GUI 

window.title("Giftlab") #setting the title for the GUI app 
window.geometry("500x500") #setting the size of the window for the GUI App

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






window.mainloop() #this makes sure that the window is created

