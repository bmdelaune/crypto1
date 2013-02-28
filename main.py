print "Welcome to the Entropy Caclulator"

file_to_work_with = raw_input("Please enter a filename to analyze: ")

file = open(file_to_work_with,"r")

text = file.read()

print text

a = {};

for c in text:
	if c<>"\n":
		if c in a:
			a[c] = a[c] + 1
		else:
			a[c] = 1

for x, y in a.iteritems():
	print x, y
