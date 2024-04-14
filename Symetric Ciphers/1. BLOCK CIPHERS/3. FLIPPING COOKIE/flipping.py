from pwn import *
import json


data = '9d2899c295518fa5cc0128978462bb163389e4eb6584476b2fc6f15ca08bfb4a062ab2c760a1b7519a69f0a70cc13196'
datareal = bytes.fromhex(data)

pt1 = b'admin=False;expi'
iv =datareal[:16]
cookie = datareal[16:]
cookie =  cookie.hex()
block = xor(pt1, iv)
cookiefake= b'admin=True;;expi' #vì True chỉ có 4 ký tự nên thêm ; để  cookiefake có số lượng ký tự = pt1 
ivfake = xor(block, cookiefake)
ivfake = ivfake.hex()

print(ivfake)
print(cookie)