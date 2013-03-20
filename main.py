import re
import sys
import os
from math import log

print "Welcome to the Entropy Caclulator"

#all_books = open("All Authors.txt","a")

for root, dirs, files in os.walk('Books'):
	for f in files:
		if f[0] <> "." and f.endswith(".txt"):
			os.system('python refined.py "'+root+"/"+f+'"')
			#print 'python refined.py "'+root+"/"+f+'"'
			print f

