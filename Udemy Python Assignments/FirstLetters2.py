def twowords(x):
	out = x.split()
	newout = [i for i in out]
	first = newout[0]
	second = newout[1]

	if first[0] == second[0]:
		return True
	else:
		return False

result = twowords("Long Reg")
print(result)

