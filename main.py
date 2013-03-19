import re
import sys
from math import log
f = open(sys.argv[1],"r")
text = f.read()
f.close()
print "Welcome to the Entropy Caclulator"

text = re.sub(r'([^\s\w]|_)+', '', text)
text = text.lower()
total_letters = len(text)
a = {}

for i, c in enumerate(text):
		if c in a:
			a[c] = a[c] + 1
		else:
			a[c] = 1

output = open(sys.argv[1]+".entropy","w")
sum = 0.0
for x, y in sorted(a.iteritems()):
	print x, y
	output.write(str(x)+": "+str(y)+"\n")
	pt = float(y) #converts key to float
	pb = float(total_letters) #converts length to float
	sum = sum + (pt/pb)*(log(pt/pb)) #calculates p(x) * log(p(x)) and adds to sum
output.close()

sum = sum*-1

print sum

