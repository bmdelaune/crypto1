print "Welcome to the Entropy Caclulator"

file_to_work_with = raw_input("Please enter a filename to analyze: ")

file = open(file_to_work_with,"r")

text = file.read()

file.close()

print text+"\n"

a = {}

for i, c in enumerate(text):
	if c<>"\n":
		if c in a:
			a[c] = a[c] + 1
		else:
			a[c] = 1
	if i+1 < len(text):
		if text[i]<>"\n" and text[i+1]<>"\n":
			if text[i]+text[i+1] in a:
				a[text[i]+text[i+1]] = a[text[i]+text[i+1]] + 1
			else:
				a[text[i]+text[i+1]] = 1
	if i+2 < len(text):
		if text[i]<>"\n" and text[i+1]<>"\n" and text[i+2]<>"\n":
			if text[i]+text[i+1]+text[i+2] in a:
				a[text[i]+text[i+1]+text[i+2]] = a[text[i]+text[i+1]+text[i+2]] + 1
			else:
				a[text[i]+text[i+1]+text[i+2]] = 1
			
output = open(file_to_work_with+".entropy","w")

for x, y in sorted(a.iteritems()):
	print x, y
	output.write(str(x)+": "+str(y)+"\n")

output.close()
	
