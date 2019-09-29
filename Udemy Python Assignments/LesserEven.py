def lessereven(a,b):
	if a%2==0 and b%2==0:
		return min(a,b)
	else:
		return max(a,b)
		pass

result = lessereven(7,4)
print(result)