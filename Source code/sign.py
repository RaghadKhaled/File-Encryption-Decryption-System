import tkinter
from tkinter import *
import bcrypt
import main
import GenerateKeys

#signup_window
def HomeWindow1():
    global Home
    main.root.withdraw()
    Home = Toplevel()
    Home.title("Simple Fileshare Application")
    width = 400
    height = 300
    screen_width =  main.root.winfo_screenwidth()
    screen_height =  main.root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    main.root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Signup!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

    lb2_home = Label(Home, text="Back to log in into the application.", font=('times new roman', 12)).pack()

# to get register in application 
def register(Username,Password):
    Username = Username
    Password = Password
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password)<=8:
        db = open("database.txt", "r")
        if Username in d:
            main.lbl_text.config(text="username already exist", fg="red") 
        elif not Username ==None: 
                    Password = Password.encode('utf-8')
                    Password = bcrypt.hashpw(Password, bcrypt.gensalt())                    
                    db = open("database.txt", "a")
                    db.write(Username+", "+str(Password)+"\n")
                    GenerateKeys.generate_keys(Username)
                    HomeWindow1()
    else:
          main.lbl_text.config(text="Password too short", fg="red")    

def Back():
    Home.destroy()
    main.root.deiconify()   