def reverse(sentence):
	new_list = sentence.split()
	#out_list = [i for i in sentence]
	reverse_list = new_list[::-1]
	return ' '.join(reverse_list)
-1
result = reverse("The lord is good")
print(result)