from tkinter import *   
import main
import RecevierDec # Raghad
import csv
def Window1():
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
    lbl_fileist = Label(Home, text="List of files you are recived", font=('times new roman', 20)).pack()
    labelframe1 = LabelFrame(Home, text="files")  
    labelframe1.pack(fill="both", expand="yes")



    file = open('ReceiversMSG.csv', 'r')
    csvreader = csv.reader(file)

    MSGList = ''
    for row in csvreader:
        if row[0] == main.USERNAME.get():
            MSGList = MSGList + row[1] + '\n'
    file.close()

    toplabel = Label(labelframe1, text=str(MSGList))  # raghad
    toplabel.pack()


    lbl_fileist = Label(Home, text="Please enter file name :", font=('times new roman', 12)).pack()
    filename = Entry(Home, textvariable=main.FILENAME, font=(10))
    filename.pack(pady=15)
    btn_open = Button(Home, text='open File', width=45, command=open1).pack(pady=15)


def Window2():
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
    lbl_fileist = Label(Home, text="The file is opened! the plaintext is", font=('times new roman', 20)).pack()
    labelframe1 = LabelFrame(Home, text=main.FILENAME.get())
    labelframe1.pack(fill="both", expand="yes")

    # Raghad decrypt start
    UserName = main.USERNAME.get()
    FileName = main.FILENAME.get()
    plaintext = RecevierDec.decrypt_file_and_key(UserName,FileName)

    bottomlabel = Label(labelframe1,text = plaintext)
    bottomlabel.pack()

    # Raghad decrypt end



def open1():
    Window2()



