from math import sqrt, floor

def fib(n):
	f = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
	return floor(f)

def sumEvenFibTerms():
	l = []
	i=1
	total = 0
	while(fib(i) < 4000000):
		l.append(fib(i))
		i+=1

	print(str(l))

	for d in l:
		if(d%2==0):
			total = total + d

	return total

print(sumEvenFibTerms())