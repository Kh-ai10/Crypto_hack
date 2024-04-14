hex_string1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
hex_string12= "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
hex_string23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
hex_string123f = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
keyhex1= bytes.fromhex(hex_string1)
keyhex23= bytes.fromhex(hex_string23)
keyhex123f = bytes.fromhex(hex_string123f)
#print(keyhex1)
flag1f = [o_f132 ^ o23 for (o_f132, o23) in zip(keyhex123f, keyhex23)]
flag = [o_f1 ^ o1 for (o_f1, o1) in zip(flag1f, keyhex1)]
flagmoi = "".join(chr(o) for o in flag)
print(flagmoi)