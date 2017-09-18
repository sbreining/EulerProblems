def reverseString(s):
	return s[::-1]

def palindromeCheck(word):
	rev_word = reverseString(word)

	if(word == rev_word):
		return True
	return False


i=999
isPal = False
product = ""
while(i>899):
	j=999
	while(j>899):
		product = str(i*j)
		isPal = palindromeCheck(product)
		if isPal:
			break
		j=j-1
	if isPal:
		break
	i=i-1

if isPal:
	print(product)
else:
	print("Nothing found")