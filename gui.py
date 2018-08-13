from tkinter import *
from PIL import Image, ImageTk
import smtplib
import pyotp
import hashlib

#########################################################################################################################
def encrypt_file():                                                 #encrypt file method
    print('this is enc executed')
    f=open('hakuna.txt','rb')
    texttoenc=f.read()
    f.close()
    texttoenc=bytearray(texttoenc)
    key = 64
    for index,value in enumerate(texttoenc):
        texttoenc[index]=value^key

    f=open('hakuna.txt','wb')
    f.write(texttoenc)
    #print(texttoenc)
    f.close()
    print('encryption is done')

def decrypt_file():                                                  #decrypt file method
    print('this is decr executed')
    f = open('hakuna.txt', 'rb')
    texttoenc = f.read()
    f.close()
    texttoenc = bytearray(texttoenc)
    key = 64
    for index, value in enumerate(texttoenc):
        texttoenc[index] = value ^ key
    #print(texttoenc)
    f = open('hakuna.txt', 'wb')
    f.write(texttoenc)
    f.close()
    print('decryption is done')



def hashin_method(passwd):                                           #password hash method
    hash_o=hashlib.sha3_512(passwd)
    #print(hash_o.hexdigest())
    f=open('hakuna.txt','w')
    f.write(hash_o.hexdigest())
    f.close()
    encrypt_file()

def return_pass(uname,upass):
    print(uname.get())
    print(upass.get())
    decrypt_file()
    hash_n = hashlib.sha3_512(upass.get().encode('utf-8'))  # pass password from tkinter here
    f = open('hakuna.txt', 'r')
    if f.readline().strip() == hash_n.hexdigest():
        f.close()
        print('You are in')  # tkinter loginpage
        return True
    else:
        encrypt_file()
    return False

def submit(win,uname,upass,fromwho):

    if fromwho == 'login':
       if return_pass(uname,upass):
           win.destroy()
           print("Submit button pressed")
           window = Tk()
           f1 = Frame(window, height=0, width=250)
           f1.pack()
           image = Image.open('tkbg.jpg')
           photo = ImageTk.PhotoImage(image)
           window.title("Client Side Password Vault")
           canvas = Canvas(window, width=500, height=400)
           canvas.create_image(200, 200, image=photo)

           canvas.pack()

           # Username
           label_user = Label(window, text="Your Vault", font=("Hekvetica", 25), fg='White', bg='#2A2A2A')
           label_user.configure(activebackground="#33B5E5", relief=FLAT)
           label_user_window = canvas.create_window(170, 50, anchor=NW, window=label_user)

           # showlistbutton
           mShow = Button(window, text='DISPLAY THE EXISTING LIST', bg='green',command=lambda: showlist(window))
           mShow.configure(width=23, activebackground="#33B5E5", relief=RAISED)
           mShow_window = canvas.create_window(160, 130, anchor=NW, window=mShow)

           # enterlistbutton
           mEnter = Button(window, text="ADD ITEM TO LIST", bg='green',command=lambda: additems(window))
           mEnter.configure(width=23, activebackground="#33B5E5", relief=RAISED)
           mEnter_window = canvas.create_window(160, 180, anchor=NW, window=mEnter)

           window.mainloop()
       else:
           exit()  #for code safety
    if fromwho == 'otp':
        win.destroy()
        print("Submit button pressed")
        window = Tk()
        f1 = Frame(window, height=0, width=250)
        f1.pack()
        image = Image.open('tkbg.jpg')
        photo = ImageTk.PhotoImage(image)
        window.title("Client Side Password Vault")
        canvas = Canvas(window, width=500, height=400)
        canvas.create_image(200, 200, image=photo)

        canvas.pack()

        # Username
        label_user = Label(window, text="Your Vault", font=("Hekvetica", 25), fg='White', bg='#2A2A2A')
        label_user.configure(activebackground="#33B5E5", relief=FLAT)
        label_user_window = canvas.create_window(170, 50, anchor=NW, window=label_user)

        # showlistbutton
        mShow = Button(window, text='DISPLAY THE EXISTING LIST', bg='green', command=lambda: showlist(window))
        mShow.configure(width=23, activebackground="#33B5E5", relief=RAISED)
        mShow_window = canvas.create_window(160, 130, anchor=NW, window=mShow)

        # enterlistbutton
        mEnter = Button(window, text="ADD ITEM TO LIST", bg='green', command=lambda: additems(window))
        mEnter.configure(width=23, activebackground="#33B5E5", relief=RAISED)
        mEnter_window = canvas.create_window(160, 180, anchor=NW, window=mEnter)

        window.mainloop()

    encrypt_file()
    exit()



def return_signup_username(win,uname,upass,cpass,email,mob):
    f=open('hakuna.txt','r')
    if f.read() != '':
        print('cant have mutiple users')
        exit()
    print(uname.get())
    print(upass.get())
    print(cpass.get())

    if upass.get()!=cpass.get():
        exit()
    else:
        passwd=upass.get().encode('utf-8')
        hashin_method(passwd)

    print(email.get())
    f=open('email.txt','w')
    f.write(email.get())
    f.close()
    print(mob.get())
    win.destroy()
    load_window()

def signuppage(win,uname,upass,cpass,email,mob):
    return_signup_username(win,uname,upass,cpass,email,mob)
    win.destroy()
    print("Signuppage button pressed")

def showlist(win):
    win.destroy()
    print("Show list button pressed")
    window = Tk()
    f1 = Frame(window, height=0, width=250)
    f1.pack()
    image = Image.open('tkbg.jpg')
    photo = ImageTk.PhotoImage(image)
    window.title("Client Side Password Vault")
    canvas = Canvas(window, width=500, height=400)
    canvas.create_image(200, 200, image=photo)
    canvas.pack()
    #labeltitle
    label_user = Label(window, text="LIST OF SITES", font=("Hekvetica", 25), fg='White', bg='#2A2A2A')
    label_user.configure(activebackground="#33B5E5", relief=FLAT)
    label_user_window = canvas.create_window(130, 30, anchor=NW, window=label_user)

    listbox = Listbox(bd=5, font=("Times", "11", "bold"), bg='#B2B2B2', relief=GROOVE, fg='black', selectborderwidth=3,
                      highlightcolor='grey',width=30)
    listbox.pack()
    f=open('hakuna.txt','r')
    items_list=f.readlines()
    for item in items_list[1:len(items_list)]:
        listbox.insert(END, item)

    listbox = canvas.create_window(120, 95, anchor=NW, window=listbox)

    # back_button

    mBackButton = Button(window, text='BACK', bg='green')
    mBackButton.configure(width=15, activebackground="#33B5E5", relief=RAISED,command=lambda:back_from_add(window))
    mBackButton_window = canvas.create_window(200, 360, anchor=NW, window=mBackButton)
    window.mainloop()

def verify_otp(mOTP,str2,win):
    str1=mOTP.get()
    if str1 == str2:
        print('Successfully Verified')
        encrypt_file()
        submit(win=win,uname=' ',upass=' ',fromwho='otp')

    else:
        print('Could Not Verify You')
        exit()

def send_otp(canvas,win,mOTP,email_id):
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    otp = totp.now()
    myotp = str(otp)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("pvault190@gmail.com", "bugsbunny@123")
    server.sendmail("pvault190@gmail.com", email_id, 'Your OTP is ' + myotp)
    mSubmitOTP = Button(win, text='SUBMIT', bg='green', command=lambda: verify_otp(mOTP,myotp,win))
    mSubmitOTP.configure(width=15, activebackground="#33B5E5", relief=RAISED)
    mSubmitOTP_window = canvas.create_window(200, 360, anchor=NW, window=mSubmitOTP)

def otp(canvas,win,mOTP):
    print("OTP button pressed")
    f=open('email.txt','r')
    email_id=f.read()
    send_otp(canvas,win,mOTP,email_id)

def dataupdated(service,passwd):
    serv=service.get()
    psd=passwd.get()
    sav="\n"+serv+"|-||-|"+psd
    f=open('hakuna.txt','a')
    f.write(sav)
    f.close()
    service.delete(0,END)
    passwd.delete(0,END)
    print("Data has been added")

def back_from_add(win):
    submit(win=win, uname=' ', upass=' ', fromwho='otp')


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
    label_user=Label(window,text="Open Vault",font=("Hekvetica",25),fg='White',bg='#2A2A2A')                       #label widget , fg means foreground color, bg means background color
    label_user.configure(activebackground="#33B5E5",relief=FLAT)                                                        #the hex color value doesnt make sense to me as it works fine without it
    label_user_window=canvas.create_window(165,120,anchor=NW,window=label_user)                                         #we add the widget over canvas rather than directly window because if we add
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
    mButton=Button(window,text='LOGIN',bg='green',command=lambda : submit(window,mUsername,mPass,'login'))
    mButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mButton_window = canvas.create_window(130, 280, anchor=NW, window=mButton)

    # ssignup_button                                                                                                    #button widget , here command=submit means when we press this button submit method will be called
    mSignupButton = Button(window, text='SIGNUP',  bg='green',command= lambda : signup(window))
    mSignupButton.configure(width=10, activebackground="#33B5E5", relief=RAISED)
    mSignupButton_window = canvas.create_window(250, 280, anchor=NW, window=mSignupButton)

    # forgotPD_button                                                                                                   #button widget , here command=submit means when we press this button submit method will be called
    mforgotButton = Button(window, text='Forgot Password?', command= lambda: otp_win(window),fg='White', bg='#2A2A2A')
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
#####################################################################################################################################

def additems(win):
    win.destroy()
    print("Add items button pressed")
    window = Tk()
    f1 = Frame(window, height=0, width=250)
    f1.pack()
    image = Image.open('tkbg.jpg')
    photo = ImageTk.PhotoImage(image)
    window.title("Client Side Password Vault")
    canvas = Canvas(window, width=500, height=400)
    canvas.create_image(200, 200, image=photo)
    # Username
    label_user = Label(window, text="Enter Fields!", font=("Hekvetica", 25), fg='White', bg='#2A2A2A')
    label_user.configure(activebackground="#33B5E5", relief=FLAT)
    label_user_window = canvas.create_window(170, 120, anchor=NW, window=label_user)

    # Enter Username
    enter_username = Label(window, text="Service", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_username.configure(relief=FLAT)
    enter_username_window = canvas.create_window(60, 190, anchor=NW, window=enter_username)

    # Username
    mUsername = Entry(font=('Helvetika', 10), bg='#d3d3d3')
    mUsername.configure(relief=FLAT)
    mUsername_window = canvas.create_window(185, 190, anchor=NW, window=mUsername)

    # Password
    mPass = Entry(show='*', font=('Helvetika', 10), bg='#d3d3d3')
    mPass.configure(relief=FLAT)
    mPass.bind('<Return>', return_pass)
    mPass_window = canvas.create_window(185, 230, anchor=NW, window=mPass)

    # Enter Pass
    enter_pass = Label(window, text="Password", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60, 230, anchor=NW, window=enter_pass)

    # submit_button
    mButton = Button(window, text='Submit', bg='green', command=lambda :dataupdated(mUsername,mPass))
    mButton.configure(width=11, activebackground="#33B5E5", relief=RAISED)
    mButton_window = canvas.create_window(160, 280, anchor=NW, window=mButton)

    # back_button

    mBackButton = Button(window, text='BACK', bg='green',command=lambda :back_from_add(window))
    mBackButton.configure(width=11, activebackground="#33B5E5", relief=RAISED)
    mBackButton_window = canvas.create_window(260, 280, anchor=NW, window=mBackButton)

    canvas.pack()
    window.mainloop()


#############################################################################################################################################

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
    enter_pass = Label(window, text="Enter Password *", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(60, 180, anchor=NW, window=enter_pass)

    # Confirm Password
    mConfrimpass = Entry(show='*', font=('Helvetika', 10),bg='#d3d3d3')
    mConfrimpass.configure(relief=FLAT)
    mConfrimpass.bind('<Return>', return_pass)
    mConfrimpass_window = canvas.create_window(185, 220, anchor=NW, window=mConfrimpass)

    # Enter confirm Pass
    enter_Confirmpass = Label(window, text="Confirm Password *", font=("TimesNewRoman", 10), fg='grey', bg='black')
    enter_Confirmpass.configure(relief=FLAT)
    enter_Confirmpass_window = canvas.create_window(60, 220, anchor=NW, window=enter_Confirmpass)

    # Email
    mEmail = Entry( font=('Helvetika', 10),bg='#d3d3d3')
    mEmail.configure(relief=FLAT)
    mEmail.bind('<Return>', return_pass)
    mEmail_window = canvas.create_window(185, 260, anchor=NW, window=mEmail)

    # Enter Email
    enter_email = Label(window, text="E-mail *", font=("TimesNewRoman", 10), fg='grey', bg='black')
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
##########################################################################################################################################


##########################################################################################################################################s

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
    otp(canvas,window,mOTP)
    window.mainloop()

load_window()