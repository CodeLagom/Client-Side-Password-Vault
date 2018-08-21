import hashlib
import inquirer
import getpass

def encrypt_file():                                                 #encrypt file method
    #print('this is enc executed')
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
    #print('encryption is done')


def decrypt_file():                                                  #decrypt file method
    #print('this is decr executed')
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
    #print('decryption is done')


def hashin_method(passwd):                                           #password hash method
    hash_o=hashlib.sha3_512(passwd)
    #print(hash_o.hexdigest())
    f=open('hakuna.txt','w')
    f.write(hash_o.hexdigest())
    f.close()
    encrypt_file()

def enter_new():                                                     #enter items method
    f=open('hakuna.txt','a')
    ans = inquirer.prompt([inquirer.Text('ans', message = "Enter your Username (Provide link to the site (if) in brackets to be specific)")]) 
    nametext = ans['ans']
    # print('Enter password: ')
    # pss=input()
    pss = input("Enter Password: ")
    str_entry='\n'+nametext+'\t\t'+pss
    f.write(str_entry)
    f.close()
    print('\n \n ~~~Successfully saved your password in the Vault~~~\n\n')
    an = inquirer.prompt([inquirer.Confirm('ans', message = "Want to Enter new Record ?")]) 
    if an['ans'] == 'y' or an['ans']== 'Y':
        enter_new()
    else:
        return

# res=input('signup or login :-') 
answer = inquirer.prompt([inquirer.List('ans', message = "Do you want to ", choices= ['Login','Signup'])])  #Asking through Inquirer
res = answer['ans']
if res == 'Signup':
    passwd = getpass.getpass('Enter Password: ').encode('utf-8')
    hashin_method(passwd)

elif res == 'Login':
    decrypt_file()
    hash_n=hashlib.sha3_512(getpass.getpass('Enter Password: ').encode('utf-8'))   #pass password from tkinter here
    f=open('hakuna.txt','r')
    if f.readline().strip() == hash_n.hexdigest():
        f.close()
        print('\n ~~~~~~~~~~~~Welcome To Your Vault~~~~~~~~~~~ \n')                                              #tkinter loginpage
        ans = inquirer.prompt([inquirer.List('ans', message = "You want to ", choices= ['Enter a new entry','View your Passwords'])]) 
        resp = ans['ans']
        if resp == 'Enter a new entry':                                                  #tkinter enter new item page
            enter_new()
        if resp == 'View your Passwords':                                                  #tkinter show list page
            f=open('hakuna.txt')
            lines=f.readlines()
            for i in range(1,len(lines)):
                print (lines[i])                                         #line by line
        encrypt_file()
    else:                                                                 #tkinter exit
        print('Failed')
        encrypt_file()
else:
    print('Invalid Response')                                            #tkinter exit

