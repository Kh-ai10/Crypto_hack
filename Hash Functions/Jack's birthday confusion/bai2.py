from math import factorial

n = pow(2,11)

for i in range(n):
	
	sx = 1 - factorial(n) / (factorial(n - i)*pow(n,i))
	if sx > 0.75:
		
		print(i)
		break