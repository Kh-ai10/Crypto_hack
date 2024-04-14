from pwn import xor
hex_string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
bytestring=bytes.fromhex(hex_string) #đổi sang bytes
print(bytestring)
kytuxor = b'' 
for b,k in zip(bytestring[:7],"crypto{".encode()): 
    kytuxor += bytes([b^k])
print (kytuxor)
print(xor(bytestring, 'myXORkey'.encode()))