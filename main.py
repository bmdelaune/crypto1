import re
import sys
import os
from math import log

print "Welcome to the Entropy Caclulator"

all_books1 = open("All Authors1.txt","w")
all_books2 = open("All Authors2.txt","w")
all_books3 = open("All Authors3.txt","w")
vertical1 = open("All Authors1.txt","w")
vertical2 = open("All Authors2.txt","w")
vertical3 = open("All Authors3.txt","w")

for root, dirs, files in os.walk('Books'):
	for f in files:
		if f[0] <> "." and f.endswith(".txt"):
			os.system('python refined.py "'+root+"/"+f+'"')
			#print 'python refined.py "'+root+"/"+f+'"'
			#print f

