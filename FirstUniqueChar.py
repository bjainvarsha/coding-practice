from collections import Counter
if __name__ == '__main__':
	value = "Mississippimmmaa"
	uniqueChar = Counter(value.lower())
	print(uniqueChar)
	flag = 0
	for char in value:
		if uniqueChar[char] == 1:
			flag = 1
			print(char)
			break
	if not flag:
		print("Not found")