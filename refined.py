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

author = re.sub('( - ).*(\.txt)','',re.sub('Books/','',sys.argv[1]))
book = re.sub('\A.*( - )','',re.sub('\.txt','',sys.argv[1]))

text = re.sub(r'([^\s\w]|_)+', '', text) #keeps only alpha/nums/space
refined = [x.lower() for x in text.split()] # makes list of lowercase words
total = ''
for word in refined: #makes a single string that contains all words pushed together
	total += word


refined1 = []
refined2 = []
refined3 = []

refined1 = split_len(total,1) #splits string into substrings of length n
refined2 = split_len(total,2) #splits string into substrings of length n
refined3 = split_len(total,3) #splits string into substrings of length n

count1 = Counter(refined1) #counts the num of occurances for each word
prob1 = defaultdict(float)
total1 = len(refined1) # total number of anything to occur

count2 = Counter(refined2) #counts the num of occurances for each word
prob2 = defaultdict(float)
total2 = len(refined2) # total number of anything to occur

count3 = Counter(refined3) #counts the num of occurances for each word
prob3 = defaultdict(float)
total3 = len(refined3) # total number of anything to occur

for key in count1.most_common(len(count1)):
	prob1[key[0]] = float(key[1]) / float(total1) # probabily of key[0] occuring
for key in count2.most_common(len(count2)):
	prob2[key[0]] = float(key[1]) / float(total2) # probabily of key[0] occuring
for key in count3.most_common(len(count3)):
	prob3[key[0]] = float(key[1]) / float(total3) # probabily of key[0] occuring

entropy1 = float(0)
entropy2 = float(0)
entropy3 = float(0)
for term in prob1:
	entropy1 += prob1[term] * math.log(prob1[term],2)
for term in prob2:
	entropy2 += prob2[term] * math.log(prob2[term],2)
for term in prob3:
	entropy3 += prob3[term] * math.log(prob3[term],2)
entropy1 *= (-1)
entropy2 *= (-1)
entropy3 *= (-1)

output = open(sys.argv[1] + ".entropy","w")
totals = open("titles.txt","a")
all_books1 = open("All Authors1.txt","a")
all_books2 = open("All Authors2.txt","a")
all_books3 = open("All Authors3.txt","a")
vertical1 = open("vertical1.txt","a")
vertical2 = open("vertical2.txt","a")
vertical3 = open("vertical3.txt","a")
for key in count1.most_common(len(count1)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ',' + str(prob1[key[0]]) + '\n')
for key in count2.most_common(len(count2)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ',' + str(prob2[key[0]]) + '\n')
for key in count3.most_common(len(count3)): #saves them to file, sorted from most to least frequent
	output.write(key[0] + ',' + str(prob3[key[0]]) + '\n')
#print '\t\t' + str(entropy1)
#print '\t\t' + str(entropy2)
#print '\t\t' + str(entropy3)
all_books1.write(str(entropy1)+"\t"+author+"\t"+book+'\n')
all_books2.write(str(entropy2)+"\t"+author+"\t"+book+'\n')
all_books3.write(str(entropy3)+"\t"+author+"\t"+book+'\n')
vertical1.write(str(entropy1)+"\t")
vertical2.write(str(entropy2)+"\t")
vertical3.write(str(entropy3)+"\t")
vertical1.close()
vertical2.close()
vertical3.close()
all_books1.close()
all_books2.close()
all_books3.close()
#totals.write("\nTotal 1:"+str(total1))
output.write('\nTotal Entropy: ' + str(entropy1))
output.write('\nTotal Entropy: ' + str(entropy2))
output.write('\nTotal Entropy: ' + str(entropy3))
output.write('\nTotal1: ' + str(total1))
output.write('\nTotal2: ' + str(total2))
output.write('\nTotal3: ' + str(total3))
output.close()

