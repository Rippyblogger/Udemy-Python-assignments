def ints(lists):
	for i in lists:
		if i == 3 and  i+1 ==3:
			return True
		else:
			return False
result = ints([1,2,3,3,4])
print (result)