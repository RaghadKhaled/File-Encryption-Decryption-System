import SenderEnc # Raghad
import main
import tkinter
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox

file_name = ''
ReciverName = ''
def on_click(error_message):
   messagebox.showerror('Python Error', error_message)

def open_text_file(text_filed):
    try:
            global file_name
            # Choose file
            text_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            # store path
            file_name = str(Path(text_file)).split('\\')[-1].split('.')[0]
            # Read file content
            text_file = open(text_file, 'r')
            # Read any additional text
            new_words = text_file.read()
            # Add any additional text to text_filed
            text_filed.insert(tkinter.END, new_words)
            # close file
            text_file.close()
            # return file name
            #return file_name
    except:
        on_click('Please select one file to send')

def save_text_file(text_filed):
    if len(file_name) > 0:
        # Choose file
        text_file_1 = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # open text_file
        text_file_1 = open(text_file_1, 'w')
        # get all text in text_filed from the first line to the end and write it on the main file
        text_file_1.write(text_filed.get(1.0, END))
    else:
        # pop up an error massege
        on_click("Please select file first")

def extraxt_names():
    options = []
    lines = []
    # Take all registered people names
    with open('database.txt') as f:
        lines = f.readlines()
    for line in lines:
        options.append(line.split(',')[0])
    return options

def send_text(recivername):

   global ReciverName
   names = extraxt_names()
   ReciverName = recivername
   if len(recivername) > 0 or len(file_name) > 0:
       if recivername in names:
           if len(file_name) > 0:
               Window4()
           else:
               # pop up an error massege
               on_click("Please select one file before send")
       else:
           # pop up an error massege
           on_click("Recevir name was not correct")
   else:
       on_click("Please select on file to send or write receiver name")


def Window3():
    # Create window
    sender_win = Tk()
    # put window at the center
    sender_win.eval('tk::PlaceWindow . center')
    # Determine title of created window
    sender_win.title("Sender window")
    # Determine size of the window and replace at the center
    width = 500
    height = 400
    screen_width = sender_win.winfo_screenwidth()
    screen_height = sender_win.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    sender_win.resizable(0, 0)
    sender_win.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # Create all labels in the window
    choose_file_name = Label(sender_win, text="Select file name :", font=('times new roman', 10))
    choose_save_file = Label(sender_win, text="Select save file :", font=('times new roman', 10))
    Describtion = Label(sender_win, text="File content", font=('times new roman', 15))
    choose_receiver_name = Label(sender_win, text="Enter receiver name :", font=('times new roman', 10))
    # Create text filed
    text_filed = Text(sender_win, width=40, height=10)
    reciver_name_text_filed = Text(sender_win, font=(8))
    # Create all buttons
    open_file_button = Button(sender_win, text="Select file", command= lambda: open_text_file(text_filed))
    save_button = Button(sender_win, text="Save file", command= lambda:save_text_file(text_filed))
    # Show all created labels
    text_filed.pack(pady=40)
    open_file_button.place(height=30, width=100, x=200, y=280)
    save_button.place(height=30, width=100, x=200, y=320)
    reciver_name_text_filed.place(height=30, width=100, x=200, y=240)
    choose_file_name.place(height=30, width=200, x=40, y=280)
    choose_save_file.place(height=30, width=200, x=40, y=320)
    choose_receiver_name.place(height=30, width=170, x=40, y=240)
    Describtion.place(height=30, width=170, x=5, y=5)



    send_file = Button(sender_win, text="Send file", command= lambda:send_text(reciver_name_text_filed.get("1.0","end-1c")))
    send_file.place(height=30, width=100, x=370, y=350)

    # Show sender window
    sender_win.mainloop()


def Window4():
    global Home
    main.root.withdraw()
    Home = Toplevel()
    Home.title("Simple Fileshare Application")
    width = 400
    height = 300
    screen_width = main.root.winfo_screenwidth()
    screen_height = main.root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main.root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_fileist = Label(Home, text="The file is sended securely! the ciphertext is", font=('times new roman', 15)).pack()
    labelframe1 = LabelFrame(Home, text=main.FILENAME.get())
    labelframe1.pack(fill="both", expand="yes")

    # Rashad encrypt start
    recivername11 = ReciverName
    FileName = file_name
    ciphertext = SenderEnc.encrypt_file_and_key(recivername11, FileName) # here I am editing

    bottomlabel = Label(labelframe1, text=ciphertext)
    bottomlabel.pack()
    # Raghad encrypt end


