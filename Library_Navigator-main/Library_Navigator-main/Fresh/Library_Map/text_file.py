from Assess import *
#defining a menu function to display the instruction
def menu():
    print("Instruction!!!")
    print("Select one of the three Options")
    print("1. Enter Subject Name")
    print("2. Enter Classmark")
    print("3. Enter Location")
menu()    
    
#defining a function to read the choice from user    
def rChoice():
    c=int(input("Enter your choice "))
    if c==1:
        subb= str(input("Enter the Subject ").upper())
        print(showSubj(subb))
    elif c==2:
        clm = str(input("Enter the classmark ").upper())
        print(showClmk(clm))
    elif c==3:
        lkt= str(input("Enter the Location ").upper()) 
        print(showLkt(lkt))
    else:
        print ("You have Entered a wrong choice")
        return c

rChoice()    