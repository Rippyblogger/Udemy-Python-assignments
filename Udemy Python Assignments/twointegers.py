def twointegers(x,y):
	if sum((x,y)) == 20 or x == 20 or y==20:
		return True
	else:
		return False

result = twointegers(20,4)
print(result)