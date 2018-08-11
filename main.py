import hashlib

def encrypt_file():
    print('this is enc executed')
    f=open('hakuna.txt','rb')
    texttoenc=f.read()
    f.close()
    texttoenc=bytearray(texttoenc)
    key = 48
    for index,value in enumerate(texttoenc):
        texttoenc[index]=value^key

    f=open('hakuna.txt','wb')
    f.write(texttoenc)
    #print(texttoenc)
    f.close()
    print('encryption is done')

def decrypt_file():
    print('this is decr executed')
    f = open('hakuna.txt', 'rb')
    texttoenc = f.read()
    f.close()
    texttoenc = bytearray(texttoenc)
    key = 48
    for index, value in enumerate(texttoenc):
        texttoenc[index] = value ^ key
    #print(texttoenc)
    f = open('hakuna.txt', 'wb')
    f.write(texttoenc)
    f.close()
    print('decryption is done')


def hashin_method(passwd):
    hash_o=hashlib.sha3_512(passwd)
    print(hash_o.hexdigest())
    f=open('hakuna.txt','w')
    f.write(hash_o.hexdigest())
    f.close()
    encrypt_file()


res=input('signup or login')
if res == 'signup':
    passwd=input('enter password').encode('utf-8')
    hashin_method(passwd)
if res == 'login':
    decrypt_file()
    hash_n=hashlib.sha3_512(input('enter your password').encode('utf-8'))
    f=open('hakuna.txt','r')
    if f.read() == hash_n.hexdigest():
        print('You are in')
        encrypt_file()
    else:
        print('Failed')
else:
    print('Invalid Response')

