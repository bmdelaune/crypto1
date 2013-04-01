from __future__ import division # this is needed for high percision floating point division
import sys
import re # regulat expressions
import math
from collections import Counter
from collections import defaultdict

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

f = open(sys.argv[1],"r")
text = f.read()
f.close()

text = re.sub(r'([^\s\w]|_)+', '', text) #keeps only alpha/nums/space
refined = [x.lower() for x in text.split()] # makes list of lowercase words
total = ''
for word in refined: #makes a single string that contains all words pushed together
	total += word
refined = split_len(total,2) #splits string into substrings of length n

count = Counter(refined) #counts the num of occurances for each word
prob = defaultdict(float)
total = len(refined) # total number of anything to occur

for key in count.most_common(len(count)):
	prob[key[0]] = float(key[1]) / float(total) # probabily of key[0] occuring

entropy = float(0)
for term in prob:
	entropy += prob[term] * math.log(prob[term],2)
entropy *= (-1)

output = open(sys.argv[1] + ".entropy","w")
totals = open("titles.txt","a")
all_books = open("All Authors.txt","a")
for key in count.most_common(len(count)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ',' + str(prob[key[0]]) + '\n')
print '\t\t' + str(entropy)
all_books.write(str(entropy)+"\t\t"+sys.argv[1]+'\n')
all_books.close()
totals.write("\n"+str(total))
output.write('\nTotal Entropy: ' + str(entropy))
output.write('\nTotal: ' + str(total))
output.close()

