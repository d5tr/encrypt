import random
from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512
from hashlib import sha224
from hashlib import sha384
from hashlib import sha3_224
from hashlib import sha3_256
from hashlib import sha3_384
from hashlib import sha3_512
from hashlib import shake_128
from hashlib import shake_256



print('''
# Thanks for use my tool #
insta : d_5tr
[1] Encrypt (MD5)
[2] Encrypt random Maximum (70)
[3] Encrypt (sha1)
[4] Encrypt (sha256)
[5] Encrypt (sha512)
[6] Encrypt (sha224)
[7] Encrypt (sha384)
[8] Encrypt (sha3_224)
[9] Encrypt (sha3_256)
[10] Encrypt (sha3_384)
[11] Encrypt (sha3_512)
[12] Encrypt (shake_128)
[13] Encrypt (shake_256)
''')
ch0s = int(input('enter number you went : '))
if ch0s == 2:
    lowen = 'qwertyuiopasdfghjklzxcvbnm'
    uppen = 'QWERTYUIOPASDFGHJKLZXCVBNM'                    #تشفير الى 70 رمز 
    numbers = '1234567890'
    symbols = '[]{+*/-_@$'

    all = lowen+uppen+numbers+symbols
    input('site went to hash : ')
    length = int(input('enter number : '))
    passwond = "".join(random.sample(all,length))
    print('------------------------')
    print(passwond)
    print('------------------------')



###################################################
elif ch0s == 1:
    import os 
    os.system("clear")



    x = input('enter you went  :')
    y = md5(x.encode()).hexdigest()                  #تشفير بقاعده
    print("-----------------------")
    print(y)
    print("-----------------------")
    print ('do you went save in file ? (yes , no) :')



##############################################
elif ch0s == 3:
    x2 = input('enter you went to hash :')
    y2 = sha1(x2.encode()).hexdigest()
    print('-----------------------')
    print(y2)
    print('-----------------------')
###############################################
elif ch0s == 4:
    x3 = input('enter you went to hash :')
    y3 = sha256(x3.encode()).hexdigest()
    print("-----------------------")
    print(y3)
    print('-----------------------')
###############################################
elif ch0s == 5:
    x4 = input('enter you went to hash :')
    y4 = sha512(x4.encode()).hexdigest()
    print("-----------------------")
    print(y4)
    print('-----------------------')
###############################################
elif ch0s == 6:
    x5 = input('enter you went to hash :')
    y5 = sha224(x5.encode()).hexdigest()
    print("-----------------------")
    print(y5)
    print('-----------------------')
###############################################
elif ch0s == 7:
    x6 = input('enter you went to hash :')
    y6 = sha384(x6.encode()).hexdigest()
    print("-----------------------")
    print(y6)
    print('-----------------------')
###############################################
elif ch0s == 8:
    x7 = input('enter you went to hash :')
    y7 = sha3_224(x7.encode()).hexdigest()
    print("-----------------------")
    print(y7)
    print('-----------------------')
##############################################
elif ch0s == 9:
    x8 = input('enter you went to hash :')
    y8 = sha3_256(x8.encode()).hexdigest()
    print("-----------------------")
    print(y8)
    print('-----------------------')
#############################################
elif ch0s == 10:
    x9 = input('enter you went to hash :')
    y9 = sha3_384(x9.encode()).hexdigest()
    print("-----------------------")
    print(y9)
    print('-----------------------')
############################################
elif ch0s == 11:
    x10 = input('enter you went to hash :')
    y10 = sha3_512(x10.encode()).hexdigest()
    print("-----------------------")
    print(y10)
    print('-----------------------')
###########################################
elif ch0s == 12:
    x11 = input('enter you went to hash :')
    y11 = shake_128(x11.encode()).hexdigest()
    print("-----------------------")
    print(y11)
    print('-----------------------')
###########################################
elif ch0s == 13 :
    x12 = input('enter you went to hash :')
    y12 = shake_256(x12.encode()).hexdigest()
    print("-----------------------")
    print(y12)
    print('-----------------------')
###########################################

