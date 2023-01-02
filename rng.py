#https://code.activestate.com/recipes/117241/
import random

def windex(lst):
	'''an attempt to make a random.choose() function that makes weighted choices

	accepts a list of tuples with the item and probability as a pair
	like: >>> x = [('one', 0.25), ('two', 0.25), ('three', 0.5)]
	>>> y=windex(x)'''
	n = random.uniform(0, 1)
	for item, weight in lst:
		if n < weight:
			break
		n = n - weight
	return item



def try_prob(num_of_times):
	x= [ ('1',0.111111111),('2',0.111111111),('3',0.111111111),('4',0.111111111),('5',0.111111111),('6',0.111111111),('7',0.111111111),('8',0.111111111),('9',0.111111111) ]
	for i in range(1,num_of_times):
		val = windex(x)
		print (str(val),end = " ")

# DRIVER CODE
#try_prob(1000000)
