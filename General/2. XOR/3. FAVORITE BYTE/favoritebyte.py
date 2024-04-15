hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
bytestring=bytes.fromhex(hex_string)
print(bytestring)
for i in range (256):
    flag= bytes([b ^ i for b in bytestring])
    print(i) 
    print(flag)
