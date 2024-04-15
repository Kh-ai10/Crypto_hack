string = 'label'
flag = ''

for c in string:
    flag += chr(ord(c) ^ 13)

print (flag)