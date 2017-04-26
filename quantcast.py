#Question : Mimic spreadsheet activity

from collections import defaultdict
import re

n, m = raw_input().split()

inp = defaultdict()

start = 65

for i in range(start, start+int(m)):
	for j in range(int(n)):
		inp[chr(i)+str(j+1)] = raw_input()

def makeExpression(x):

	terms = re.findall("([-+*/]|[A-Z][0-9]+|[0-9]+\.[0-9]+|[0-9]+)", x)

	if len(terms) == 1:
		new_terms = findValue(terms[0])

	else:
		for i in range(len(terms)):
			if re.match("([-+*/])", terms[i]) != None:
				temp = terms[i]
				terms[i] = findValue(terms[i-1])
				terms[i-2] = findValue(terms[i-2]) 
				terms[i-1] = temp
				exp = " ".join(terms[i-2:i+1])
				break
		new_terms = " ".join(terms[:i-2])+" "+str(eval(exp))+" "+" ".join(terms[i+1:])
	return new_terms

def findValue(num):
	try:
		num = str(float(num))
	except ValueError:
		try:
			num = str(inp[num])
		except KeyError:
			num = '0'
	return num

count = 0
flag = 1

while(flag != 0 and count <= int(m)*int(n)):
	flag = 0
	count = count+1
	for (key, val) in inp.items():
		try:
			inp[key] = makeExpression(val)
			x = eval(makeExpression(val))

		except (SyntaxError, NameError):
			flag = 1
			pass
try:
	for (key, val) in inp.items():
			print(format(float(val), '.5f'))
except ValueError:
	print("Error: Circular dependency!")






