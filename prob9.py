product = 0
for a in range(1,1001):
	print(a)
	for b in range(a+1,1001):
		for c in range(b+1,1001):
			if ((a**2 + b**2) == c**2):
				if((a + b + c) == 1000):
					product = a*b*c

print(product)