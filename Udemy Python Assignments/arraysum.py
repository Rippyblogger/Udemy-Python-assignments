def arraysum(*args):
	newlist = [x for x in args]
	for i in newlist:
		#if i==6 and (i[i+1],i[1+2],i[i+3]) in (7,8,9):
		if i!=6 and (i[i+1],i[1+2],i[i+3]) not in ((7,8,9)):
			return sum(newlist)
		else:
			return "Drum"



resutl = arraysum(14,5,6,7,8,12)
print(resutl)
