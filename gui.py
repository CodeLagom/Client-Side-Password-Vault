from tkinter import *
from PIL import Image, ImageTk




def load_window():                                                                                                      # method definition to load  our software window
    window=Tk()                                                                                                         # creates a window to work on in tkinter stuff
    image=Image.open('tkbg.jpg')                                                                                        # our image in the directory this program is in
    photo=ImageTk.PhotoImage(image)                                                                                     # converts it into usable form to use in tkinter
    window.title("Client Side Password Vault")                                                                          # name that appears on statusbar
    canvas=Canvas(window,width=500,height=400)                                                                          # creates a canvas in window , canvas only does work of showing an image
    canvas.create_image(200,200,image=photo)                                                                            # we load our background image
    canvas.pack()                                                                                                       # pack() method adds the widget into our window

    #Username
    label_user=Label(window,text="Hello, Username",font=("Hekvetica",25),fg='White',bg='#2A2A2A')                      #label widget , fg means foreground color, bg means background color
    label_user.configure(activebackground="#33B5E5",relief=FLAT)                                                       #the hex color value doesnt make sense to me as it works fine without it
    label_user_window=canvas.create_window(125,120,anchor=NW,window=label_user)                                        #we add the widget over canvas rather than directly window because if we add
                                                                                                                       #directly to window it would get hidden behind canvas
    # Enter Username                                                                                                   #label widget
    enter_pass = Label(window, text="Username", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60, 190, anchor=NW, window=enter_pass)

    # Username
    mPass = Entry(show='*', font=('Helvetika', 10), bg='#d3d3d3')                                                       # same thing except widget is entry type means takes text input
    mPass.configure(relief=FLAT)
    mPass_window = canvas.create_window(175, 190, anchor=NW, window=mPass)

    #Password
    mPass=Entry(show='*',font=('Helvetika',10),bg='#d3d3d3')                                                            #same thing except widget is entry type means takes text input
    mPass.configure(relief=FLAT)
    mPass.bind('<Return>',return_pass)
    mPass_window = canvas.create_window(175, 230, anchor=NW, window=mPass)

    #Enter Pass                                                                                                         #label widget
    enter_pass=Label(window, text="Enter Password", font=("TimesNewRoman", 10),fg='grey',bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60,230, anchor=NW, window=enter_pass)

    #submit_button                                                                                                      #button widget , here command=submit means when we press this button submit method will be called
    mButton=Button(window,text='LOGIN',bg='green',command=submit)
    mButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mButton_window = canvas.create_window(130, 280, anchor=NW, window=mButton)

    # ssignup_button                                                                                                    #button widget , here command=submit means when we press this button submit method will be called
    mButton = Button(window, text='SIGNUP',  bg='green',command= lambda : submit(window,mPass))
    mButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mButton_window = canvas.create_window(250, 280, anchor=NW, window=mButton)

    # forgotPD_button                                                                                                   #button widget , here command=submit means when we press this button submit method will be called
    mButton = Button(window, text='Forgot Password?', command=forgotpassword,fg='White', bg='#2A2A2A')
    mButton.configure(width=15, activebackground="#33B5E5", relief=FLAT)
    mButton_window = canvas.create_window(130, 320, anchor=NW, window=mButton)

    # otp_button                                                                                                        #button widget , here command=submit means when we press this button submit method will be called
    mButton = Button(window, text='OTP', command=otp,fg='White', bg='#2A2A2A')
    mButton.configure(width=5, activebackground="#33B5E5", relief=FLAT)
    mButton_window = canvas.create_window(280, 320, anchor=NW, window=mButton)

    #window_launch
    f1=Frame(window, height=0, width=150)                                                                               #the height and width here doesnt make much sense to me
    f1.pack()                                                                                                           # better way take approx values , add background image then reduce values till satisfied
    window.mainloop()
    # keeps window open till not closed by user

def submit(win,paswd):
    return_pass(paswd)
    win.destroy()
    print("Submit button pressed")
    window = Tk()
    f1 = Frame(window, height=0, width=250)                                                                             # the height and width here doesnt make much sense to me
    f1.pack()
    image = Image.open('tkbg.jpg')                                                                                      # our image in the directory this program is in
    photo = ImageTk.PhotoImage(image)                                                                                   # converts it into usable form to use in tkinter
    window.title("Client Side Password Vault")                                                                          # name that appears on statusbar
    canvas = Canvas(window, width=500,height=400)                                                                       # creates a canvas in window , canvas only does work of showing an image
    canvas.create_image(200, 200, image=photo)

    canvas.pack()
    # Username
    label_user = Label(window, text="LOGGED IN SUCESSFULLY!", font=("Hekvetica", 10),
                       fg='blue')                                                                                       # label widget , fg means foreground color, bg means background color
    label_user.configure(activebackground="#33B5E5", relief=FLAT, width=30)                                             # the hex color value doesnt make sense to me as it works fine without it
    label_user_window = canvas.create_window(125, 120, anchor=NW, window=label_user)
    window.mainloop()

def return_pass(en):
        print(en.get())




def signup():
    print("Signup button pressed")

def forgotpassword():
    print("Forgotpassword button pressed")

def otp():
    print("OTP button pressed")
load_window()