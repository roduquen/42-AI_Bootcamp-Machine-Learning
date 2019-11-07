import string

def		text_analyzer(*parameter):
	text = ""
	if len(parameter) > 1:
		print("There is too much parameters.")
		return
	if parameter:
		text = parameter[0]
	while not text:
		print("What is the text to analyze ?")
		text = input(">> ")
	if len(text) == 1:
		char = " character:"
	else:
		char = " characters:"
	print("The text countains " + str(len(text)) + char)
	uppercase = sum(map(str.isupper, text))
	lowercase = sum(map(str.islower, text))
	space = sum(map(str.isspace, text))
	punc = 0
	for letter in string.punctuation:
		punc = punc + text.count(letter)
	if uppercase:
		print("- " + str(uppercase) + " upper letters")
	if lowercase:
		print("- " + str(lowercase) + " lower letters")
	if punc:
		print("- " + str(punc) + " punctuations marks")
	if space:
		print("- " + str(space) + " spaces")
