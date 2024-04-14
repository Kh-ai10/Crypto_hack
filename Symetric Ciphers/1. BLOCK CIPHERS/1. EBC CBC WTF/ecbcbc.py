from Crypto.Util.number import *
from pwn import xor
cipher_hex='69bd314fb6a1adda90f73362651847b9ede33d2298398aa6594201071a0c83bb799864b0a0586d81c1e217834aae95cb'
cipher=bytes.fromhex(cipher_hex)
cipher_blocks=[ cipher[i:i+16] for i in range(0,len(cipher),16) ]
decrypted_hex='93832121365bf8ac0f60d72fcd83f0b70acf483fc2ced6e9f3956c57107b2c8cb2d74b12a95dd5976e1d20263b2da2c6'
decrypted=bytes.fromhex(decrypted_hex)
decrypt_blocks=[ decrypted[i:i+16] for i in range(0,len(decrypted),16) ]
part1=(xor(decrypt_blocks[1],cipher_blocks[0]))
part2=(xor(decrypt_blocks[2],cipher_blocks[1]))
print((part1+part2).decode())