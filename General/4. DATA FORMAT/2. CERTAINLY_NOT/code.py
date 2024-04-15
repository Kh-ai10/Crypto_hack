from Crypto.PublicKey import RSA
## chuyển der file sang crt file bằng tool https://www.sslshopper.com/ssl-converter.html 
## chứng chỉ bảo mật SSL có phần mở rộng tệp là crt hoăc pem
with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.crt','r') as file:
    key = RSA.import_key(file.read())
    print(type(key))
    print(key.n)