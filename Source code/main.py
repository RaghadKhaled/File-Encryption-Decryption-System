import tkinter
from tkinter import *
import sign
import login

#Setting up the Main Frame
root = Tk()
root.title("Python: Simple Fileshar Application")
width = 500
height = 400 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#Designing the Layout

#VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
FILENAME = StringVar()
RECIVERNAME = StringVar() # Raghad
RNAME = StringVar()
#FRAMES
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=400)
Form.pack(side=TOP, pady=20)

#LABELS
lbl_title = Label(Top, text = "Python: Simple Fileshare Application", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#ENTRY WIDGETS
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

def Login(event=None):
		login.gainAccess(USERNAME.get(),PASSWORD.get())

def signup(event=None):
		sign.register(USERNAME.get(),PASSWORD.get())

#BUTTON WIDGETS
btn_login = Button(Form, text="Login", width=45, command = Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

btn_signup = Button(Form, text="Signup", width=45, command = signup)
btn_signup.grid(pady=25, row=4, columnspan=2)
btn_signup.bind('<Return>', signup)

#Initializing the Application 
if __name__ == '__main__':
    root.mainloop()