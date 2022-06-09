import tkinter
from tkinter import *
import bcrypt
import main
import reciverGUI
import senderGUI

# login_window  
def HomeWindow():
    global Home
    main.root.withdraw()
    Home = Toplevel()
    Home.title("Simple Fileshare Application")
    width = 500
    height = 400
    screen_width = main.root.winfo_screenwidth()
    screen_height = main.root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    main.root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Welcome", font=('times new roman', 20)).pack()
    btn_send = Button(Home, text='Send File', width=45, command=send).pack(pady=15)
    btn_recive = Button(Home, text='Recive File', width=45, command=recive).pack(pady=15)

# to get access to application 
def gainAccess(Username, Password):
    Username1 = Username
    Password1 = Password
    
    if not len(Username1 or Password1) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username1 in data:
                    hashed = data[Username1].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password1.encode(), hashed):
                            HomeWindow()
                        else:
                            main.lbl_text.config(text="Invalid username or password", fg="red")
                        
                    except:
                        main.lbl_text.config(text="Incorrect passwords or username", fg="red")
                else:
                   main.lbl_text.config(text="Username doesn't exist", fg="red")
            except:
             main.lbl_text.config(text="Password or username doesn't exist", fg="red")
        else:
         main.lbl_text.config(text="Error logging into the system", fg="red")        
    else:
     main.lbl_text.config(text="Please attempt login again", fg="red")



def send():
    senderGUI.Window3()


def recive():
    reciverGUI.Window1()