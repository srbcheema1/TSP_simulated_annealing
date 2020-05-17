from random import randint
import sys

n = 30
if(len(sys.argv) == 2):
	n = int(sys.argv[1])

for _ in range(n):
	a = randint(1,50)
	b = randint(1,50)
	print(a,b)