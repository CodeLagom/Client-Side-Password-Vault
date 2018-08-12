from tkinter import *
from PIL import Image, ImageTk
import smtplib
import pyotp
import time

#########################################################################################################################

def return_pass(uname,upass):
    print(uname.get())
    print(upass.get())

def submit(win,uname,upass):
    return_pass(uname,upass)
    win.destroy()
    print("Submit button pressed")
    window = Tk()
    f1 = Frame(window, height=0, width=250)
    f1.pack()
    image = Image.open('tkbg.jpg')
    photo = ImageTk.PhotoImage(image)
    window.title("Client Side Password Vault")
    canvas = Canvas(window, width=500,height=400)
    canvas.create_image(200, 200, image=photo)

    canvas.pack()
    # Username
    label_user = Label(window, text="LOGGED IN SUCESSFULLY!", font=("Hekvetica", 10),fg='blue')
    label_user.configure(activebackground="#33B5E5", relief=FLAT, width=30)
    label_user_window = canvas.create_window(125, 120, anchor=NW, window=label_user)
    window.mainloop()

def return_signup_username(win,uname,upass,cpass,email,mob):
    print(uname.get())
    print(upass.get())
    print(cpass.get())
    print(email.get())
    f=open('email.txt','w')
    f.write(email.get())
    f.close()
    print(mob.get())

def signuppage(win,uname,upass,cpass,email,mob):
    return_signup_username(win,uname,upass,cpass,email,mob)
    win.destroy()
    print("Signuppage button pressed")


def forgotpassword():
    print("Forgotpassword button pressed")

def send_otp(email_id):
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    otp = totp.now()
    myotp = str(otp)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("phantomfive11@gmail.com", "<enter-password-here>")
    server.sendmail("phantomfive11@gmail.com", email_id, 'Your OTP is ' + myotp)
    time.sleep(15)
    otp = ""


def otp():
    print("OTP button pressed")
    f=open('email.txt','r')
    email_id=f.read()
    send_otp(email_id)

########################################################################################################################

def load_window():                                                                                                      # method definition to load  our software window
    window=Tk()                                                                                                         # creates a window to work on in tkinter stuff
    image=Image.open('tkbg.jpg')                                                                                        # our image in the directory this program is in
    photo=ImageTk.PhotoImage(image)                                                                                     # converts it into usable form to use in tkinter
    window.title("Client Side Password Vault")                                                                          # name that appears on statusbar
    canvas=Canvas(window,width=500,height=400)                                                                          # creates a canvas in window , canvas only does work of showing an image
    canvas.create_image(200,200,image=photo)                                                                            # we load our background image
    canvas.pack()                                                                                                       # pack() method adds the widget into our window

    #Username
    label_user=Label(window,text="Hello, Username",font=("Hekvetica",25),fg='White',bg='#2A2A2A')                       #label widget , fg means foreground color, bg means background color
    label_user.configure(activebackground="#33B5E5",relief=FLAT)                                                        #the hex color value doesnt make sense to me as it works fine without it
    label_user_window=canvas.create_window(125,120,anchor=NW,window=label_user)                                         #we add the widget over canvas rather than directly window because if we add
                                                                                                                        #directly to window it would get hidden behind canvas
    # Enter Username                                                                                                    #label widget
    enter_username = Label(window, text="Username", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_username.configure(relief=FLAT)
    enter_username_window = canvas.create_window(60, 190, anchor=NW, window=enter_username)

    # Username
    mUsername = Entry(font=('Helvetika', 10), bg='#d3d3d3')                                                             # same thing except widget is entry type means takes text input
    mUsername.configure(relief=FLAT)
    mUsername_window = canvas.create_window(185, 190, anchor=NW, window=mUsername)

    #Password
    mPass=Entry(show='*',font=('Helvetika',10),bg='#d3d3d3')                                                            #same thing except widget is entry type means takes text input
    mPass.configure(relief=FLAT)
    mPass.bind('<Return>',return_pass)
    mPass_window = canvas.create_window(185, 230, anchor=NW, window=mPass)

    #Enter Pass                                                                                                         #label widget
    enter_pass=Label(window, text="Enter Password", font=("TimesNewRoman", 10),fg='grey',bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60,230, anchor=NW, window=enter_pass)

    #submit_button                                                                                                      #button widget , here command=submit means when we press this button submit method will be called
    mButton=Button(window,text='LOGIN',bg='green',command=lambda : submit(window,mUsername,mPass))
    mButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mButton_window = canvas.create_window(130, 280, anchor=NW, window=mButton)

    # ssignup_button                                                                                                    #button widget , here command=submit means when we press this button submit method will be called
    mSignupButton = Button(window, text='SIGNUP',  bg='green',command= lambda : signup(window))
    mSignupButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mSignupButton_window = canvas.create_window(250, 280, anchor=NW, window=mSignupButton)

    # forgotPD_button                                                                                                   #button widget , here command=submit means when we press this button submit method will be called
    mforgotButton = Button(window, text='Forgot Password?', command=forgotpassword,fg='White', bg='#2A2A2A')
    mforgotButton.configure(width=15, activebackground="#33B5E5", relief=FLAT)
    mforgotButton_window = canvas.create_window(130, 320, anchor=NW, window=mforgotButton)

    # otp_button                                                                                                        #button widget , here command=submit means when we press this button submit method will be called
    mOtpButton = Button(window, text='OTP', command= lambda :otp_win(window),fg='White', bg='#2A2A2A')
    mOtpButton.configure(width=5, activebackground="#33B5E5", relief=FLAT)
    mOtpButton_window = canvas.create_window(280, 320, anchor=NW, window=mOtpButton)

    #window_launch
    f1=Frame(window, height=0, width=150)                                                                               #the height and width here doesnt make much sense to me
    f1.pack()                                                                                                           # better way take approx values , add background image then reduce values till satisfied
    window.mainloop()
                                                                                                                        # keeps window open till not closed by user


def signup(win):
    win.destroy()
    print("Signup button pressed")
    window = Tk()
    f1 = Frame(window, height=0, width=250)
    f1.pack()
    image = Image.open('tkbg.jpg')
    photo = ImageTk.PhotoImage(image)
    window.title("Client Side Password Vault")
    canvas = Canvas(window, width=500,height=400)
    canvas.create_image(200, 200, image=photo)

    # HELLO USERNAME
    label_user = Label(window, text="Hello, User!", font=("Hekvetica", 25), fg='White',bg='#2A2A2A')
    label_user.configure(activebackground="#33B5E5", relief=FLAT)
    label_user_window = canvas.create_window(130, 60, anchor=NW, window=label_user)

    # Enter Username
    enter_username = Label(window, text="Username", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_username.configure(relief=FLAT)
    enter_username_window = canvas.create_window(60, 140, anchor=NW, window=enter_username)

    # Username
    mPass = Entry(font=('Helvetika', 10), bg='#d3d3d3')
    mPass.configure(relief=FLAT)
    mPass_window = canvas.create_window(185, 140, anchor=NW, window=mPass)

    # Password
    mPassword = Entry(show='*', font=('Helvetika', 10),bg='#d3d3d3')
    mPassword.configure(relief=FLAT)
    mPassword.bind('<Return>', return_pass)
    mPassword_window = canvas.create_window(185, 180, anchor=NW, window=mPassword)

    # Enter Pass
    enter_pass = Label(window, text="Enter Password", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60, 180, anchor=NW, window=enter_pass)

    # Confirm Password
    mConfrimpass = Entry(show='*', font=('Helvetika', 10),bg='#d3d3d3')
    mConfrimpass.configure(relief=FLAT)
    mConfrimpass.bind('<Return>', return_pass)
    mConfrimpass_window = canvas.create_window(185, 220, anchor=NW, window=mConfrimpass)

    # Enter confirm Pass
    enter_Confirmpass = Label(window, text="Confirm Password", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_Confirmpass.configure(relief=FLAT)
    enter_Confirmpass_window = canvas.create_window(60, 220, anchor=NW, window=enter_Confirmpass)

    # Email
    mEmail = Entry( font=('Helvetika', 10),bg='#d3d3d3')
    mEmail.configure(relief=FLAT)
    mEmail.bind('<Return>', return_pass)
    mEmail_window = canvas.create_window(185, 260, anchor=NW, window=mEmail)

    # Enter Email
    enter_email = Label(window, text="E-mail", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_email.configure(relief=FLAT)
    enter_email_window = canvas.create_window(60, 260, anchor=NW, window=enter_email)

    # Number
    mNumber = Entry(font=('Helvetika', 10), bg='#d3d3d3')
    mNumber.configure(relief=FLAT)
    mNumber.bind('<Return>', return_pass)
    mNumber_window = canvas.create_window(185, 300, anchor=NW, window=mNumber)

    # Enter Number
    enter_number = Label(window, text="Phone Number", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_number.configure(relief=FLAT)
    enter_number_window = canvas.create_window(60, 300, anchor=NW, window=enter_number)
    canvas.pack()

    # signup_button

    mSignupButton = Button(window, text='SIGNUP', bg='green', command= lambda : signuppage(window,mPass,mPassword,
                                                                                mConfrimpass,mEmail,mNumber))
    mSignupButton.configure(width=15, activebackground="#33B5E5", relief=RAISED)
    mSignupButton_window = canvas.create_window(200, 360, anchor=NW, window=mSignupButton)


    window.mainloop()


def otp_win(win):
    win.destroy()
    window = Tk()
    f1 = Frame(window, height=0, width=250)
    f1.pack()
    image = Image.open('tkbg.jpg')
    photo = ImageTk.PhotoImage(image)
    window.title("Client Side Password Vault")
    canvas = Canvas(window, width=500, height=400)
    canvas.create_image(200, 200, image=photo)

    # Enter Your OTP
    label_user = Label(window, text="Enter Your OTP", font=("Hekvetica", 25), fg='White', bg='#2A2A2A')
    label_user.configure(activebackground="#33B5E5", relief=FLAT)
    label_user_window = canvas.create_window(130, 60, anchor=NW, window=label_user)

    #OTP_Entry
    mOTP = Entry(font=('Helvetika', 10), bg='#d3d3d3')
    mOTP.configure(relief=FLAT)
    mOTP_window = canvas.create_window(185, 140, anchor=NW, window=mOTP)

    canvas.pack()
    window.mainloop()

load_window()