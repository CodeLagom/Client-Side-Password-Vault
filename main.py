import hashlib

def hashin_method(passwd):
    hash_o=hashlib.sha3_512(passwd)
    print(hash_o.hexdigest())
    f=open('hakuna.txt','w')
    f.write(hash_o.hexdigest())
    f.close()


res=input('signup or login')
if res == 'signup':
    passwd=input('enter password').encode('utf-8')
    hashin_method(passwd)
else:
    hash_n=hashlib.sha3_512(input('enter your password').encode('utf-8'))
    f=open('hakuna.txt','r')
    if f.read() == hash_n.hexdigest():
        print('You are in')
    else:
        print('Failed')

