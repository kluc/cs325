import time
import getopt
import sys

list = [0, 43, 43, 5 ,6 ,7, 7,90]


def main(argv):
	try:
		opts, args = getopt.getopt(argv, "p:", ["problem="])
	except getopt.GetoptError:
		print "something in the water"
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ("-p", "--problem") and arg == "1":
			p1()
		elif opt == "-p" and arg == '2':
			p2()
			
			
			
def p1():
	print "Brute Force Sorting"
	lowest = 9999999
	print list
	sortedlist = []
	while len(list) != 0:
		lowest = 9999999
		for x in list:
			if x < lowest:
				lowest = x
		sortedlist.append(lowest)
		list.remove(lowest)
	print sortedlist

def p2():
	print "Mergesort"
	print list
	mergesort(list)

def mergesort(a):
	if len(a) > 1:
		mid = len(a) / 2
		print merge(mergesort(a[0:mid]), mergesort(a[mid + 1:]))
	else:
		return a
	

def merge(x, y):
	if len(x) == 0:
		return y
	if len(y) == 0:
		return x
	
	if x[0] <= y[0]:
		temp = [x[0]]
		#return merge(x[1:], y).insert(0, x[0])
		return temp + merge(x[1:], y)
		
	elif x[0] > y[0]:
		temp = [y[0]]
		return temp + merge(x, y[1:])
		#return merge(x, y[1:]).insert(0, y[0])
	
	
if __name__ == "__main__":
	main(sys.argv[1:])