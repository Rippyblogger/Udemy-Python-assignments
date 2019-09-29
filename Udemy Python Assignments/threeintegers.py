def threeintegers(a,b,c):

	if ((a or b or c) in range(1,12)):
		if (sum((a,b,c)) <= 21):
			return sum((a,b,c))
	else:
		return("Please pick a number between 1 and 11")

	#elif ((a,b,c) in range(0,12) and sum(a,b) > 2 and (a,b,c) == 11:
	#	return sum(a,b,c) - 10
	#else:
	#	return "BUST"
		


result = threeintegers(2,1,10)
print(result)