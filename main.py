import hashlib

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

def enter_new():                                                     #enter items method
    f=open('hakuna.txt','a')
    print('enter item name: ')
    nametext=input()
    print('enter password: ')
    pss=input()
    str_entry='\n'+nametext+'\t\t'+pss
    f.write(str_entry)
    f.close()
    print('done')
    print('Add More ?')
    if input() == 'yes':
        enter_new()
    else:
        return

res=input('signup or login')                                             #tkinter first page
if res == 'signup':
    passwd=input('enter password').encode('utf-8')
    hashin_method(passwd)

elif res == 'login':
    hash_n=hashlib.sha3_512(input('enter your password').encode('utf-8'))   #pass password from tkinter here
    f=open('hakuna.txt','r')
    decrypt_file()
    if f.readline().strip() == hash_n.hexdigest():
        f.close()
        print('You are in')                                              #tkinter loginpage
        print('1- enter new item\n 2-see your list ')
        resp=input()
        if resp == '1':                                                  #tkinter enter new item page
            enter_new()
        if resp == '2':                                                  #tkinter show list page
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

