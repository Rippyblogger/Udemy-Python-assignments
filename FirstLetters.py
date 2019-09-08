def twoword(x):
	
	out = x.split()
	Firstword = out[0]
	Secondword = out[1]


	if Firstword[0] == Secondword[0]:
		return True
	else:
		return False

result = twoword("Lengthy Bung")
print (result)