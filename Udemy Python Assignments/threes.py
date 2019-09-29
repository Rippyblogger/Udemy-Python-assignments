def threes(word):
	newlist = [x for x in word]
	finallist = []
	for i in newlist:
		finallist.append(i * 3)
	return "".join(finallist)

result = threes("storm")
print(result)
