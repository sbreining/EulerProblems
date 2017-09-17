
for num in range(600851475143,0,-1):
	print(num)
	prime = True
	for i in range(2,num):
		print(i)
		if( (num%i) == 0 ):
			prime = False
	if prime:
		print(num)
		break
