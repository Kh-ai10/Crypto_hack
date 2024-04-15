from Crypto.PublicKey import RSA
with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem','r') as key_file:
    key = RSA.importKey(key_file.read())
    print(key.d)