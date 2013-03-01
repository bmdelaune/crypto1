import sys
import re
from math import log
from collections import Counter

f = open(sys.argv[1],"r")
text = f.read()
f.close()

text = re.sub(r'([^\s\w]|_)+', '', text) #keeps only alpha/nums/space
refined = [x.lower() for x in text.split()] # makes list of lowercase words
total_words = len(refined)
count = Counter(refined) #counts the num of occurances for each word

output = open(sys.argv[1] + ".entropy","w")
sum = 0.0
for key in count.most_common(len(count)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ' : ' + str(key[1]) + '\n')
	pt = float(key[1]) #converts key to float
	pb = float(total_words) #converts length to float
	sum = sum + (pt/pb)*(log(pt/pb)) #calculates p(x) * log(p(x)) and adds to sum
output.close()

sum = sum*-1

print "The entropy of "+sys.argv[1]+" is "+str(sum)+"."
	
