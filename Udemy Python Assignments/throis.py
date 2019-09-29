def throis(a,b,c):
	if sum((a,b,c)) <= 21:
		return sum((a,b,c))
	elif (sum((a,b,c)) > 21) and 11 in (a,b,c):
		return sum((a,b,c)) - 10
	#elif (sum((a,b,c)) >= 21) and (a or b or c == 11)  :
		#exceedsum = sum((a,b,c)) - 10
	else:
		return "BUST"


result = throis(2,11,10)
print(result)