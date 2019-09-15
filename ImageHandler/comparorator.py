from opencvim import image_to_text, dic_pic

def str_to_lis(text):
	lis = []
	i = 0
	last = 0
	word = ''
	while i<len(text):
		if text[i] == ' ' or text[i] == '\n':
			word = text[last:i]
			last = i+1
			if word != '':
				lis.append(word)
		i+=1
	lis.append(text[last:])
	return lis

#frequencyb dictionary and second_pic should be a list of words
def compare(freq_dic, second_pic):
	i = 0
	last = 0
	diff = 0
	second_pic_lis = str_to_lis(second_pic)
	# print(second_pic_lis)
	for word in second_pic_lis:
		if word in freq_dic:
			if freq_dic[word] > 0:
				freq_dic[word] -= 1
			else: 
				diff += 1
		else:
			diff += 1
		i+=1
	if diff/len(second_pic_lis)>0.5:
		print(diff)
		return True
	else:
		return False

# text = "Hello this is fun. I live in hell."
# text2 = "Hello this is horrible. I love heaven."
# dic1 = dic_pic(text)
# print(compare(dic1, text2))
# print(str_to_lis(text))