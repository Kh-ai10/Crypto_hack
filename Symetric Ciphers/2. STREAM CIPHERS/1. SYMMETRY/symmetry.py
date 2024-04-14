import requests
data = '5a56630e12a8900a3760b544767fbff144fc505a5f742b7450d7aa0bf88f30b8a8376fed0192b50f26c0dd86ac3049bf76'
iv=data[:32]
ciphertext=data[32:]
print(iv)
print(ciphertext)

