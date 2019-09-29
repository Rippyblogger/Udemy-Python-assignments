def myfunc(*bots):
	mylist = []
	for i in bots:
		if i%2==0 and i != 0:
			mylist.append(i)
	return mylist

myfunc(0,2,3,4)
Result = myfunc(0,2,3,4);
print(Result)