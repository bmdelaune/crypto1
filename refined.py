import sys
import re
from collections import Counter

f = open(sys.argv[1],"r")
text = f.read()
f.close()

text = re.sub(r'([^\s\w]|_)+', '', text) #keeps only alpha/nums/space
refined = [x.lower() for x in text.split()] # makes list of lowercase words
count = Counter(refined) #counts the num of occurances for each word

output = open(sys.argv[1] + ".entropy","w")
for key in count.most_common(len(count)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ' : ' + str(key[1]) + '\n')
output.close()
	
