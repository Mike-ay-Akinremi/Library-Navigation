
import tkinter as tk
from Library_Map.Assess import * #import python file here 

root = tk.Tk()
root.iconbitmap("keele-university-logo.ico") # displays the university's logo.
root.geometry("300x400")                     # creates a widgets

def task1():
    def sub():
        result = showSubj(subinput.get()) #call in subject function code here
        pass
    subject = tk.Label(root, text = "Subject name").grid()
    subinput = tk.StringVar()
    print(subinput.get) 
    subjectinput = tk.Entry(root, textvariable = subinput).grid() 
    tk.Button(text = "submit", command = sub).grid()
    output = tk.Label(root, text = " ")
    output.grid()

def task2():
    def cls():
        result = showClmk(classinput.get()) #call in classmark function code here
        pass
    classmark = tk.Label(root, text = "Classmark").grid()
    classinput = tk.StringVar()
    classmarkinput = tk.Entry(root, textvariable= classinput).grid()
    tk.Button(text = "submit", command = cls).grid()
    output = tk.Label(root, text = " ")
    output.grid()


def task3():
    def loc():
        result = showLkt(locinput.get()) # call in location function code here
        pass
    location = tk.Label(root, text = "Location").grid()
    locinput = tk.StringVar()
    locationinput = tk.Entry(root, textvariable= locinput).grid()
    result = tk.Label(root, text=' ')
    result.grid()

tk.Label(root, text ="Keele University Library Navigator", 
         font="timenewroman 12  bold", bg='white').grid()
tk.Label(root, text = "Select any of the three options given").grid()


tk.Button(text = "Subjects", command = task1).grid()
tk.Button(text = "Classmarks", command = task2).grid()
tk.Button(text = "Locations", command = task3).grid()

root.mainloop()