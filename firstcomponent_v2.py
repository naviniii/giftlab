#this is my second version for my first component


#this is my first version of my first component


from tkinter import*

window = Tk() #creating the window for the GUI 

window.title("Giftlab") #setting the title for the GUI app 
window.geometry("500x500") #setting the size of the window for the GUI App


def check_entry(): 
  print(check)

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



#creating buttons

quitbtn = Button(window, text = "Quit", command = root.destroy) #root.destroy means the program will close
quitbtn.pack()


findgift_btn = Button(window, text = "Find A Gift!", command = giftfinder)
#gift finder is just a temporary name, until I build a function which properly represents moving to the next component. 



window.mainloop() #this makes sure that the window is created
