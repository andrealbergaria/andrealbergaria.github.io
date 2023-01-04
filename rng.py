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


#WORKS
#Gets 2 probabilities (one function from python, another one mine)
# and writes 100 bytes to file
# to test do end -c random_file.bin (linux app ..debian -> just apt install ent)


def try_probability_library(num_bytes):
	with open("random_file_lib.bin", "wb") as binary_file:
		result_list = []
		for i in range(1,256):
			val = random.randint(0,256)
			result_list.append(val)
		arr = bytearray(result_list)
		binary_file.write(arr)

try_probability_library(100)

def try_probability_bytes(num_of_bytes):
	with open("random_file.bin", "wb") as binary_file:

		# Each byte gets 1/256 -> 0.00390625
		lst = [ (0,0.00390625)]
		for i in range(1,256):
			lst.append( (i,0.00390625))

		res_list = []
		for i in range(1,num_of_bytes):
			val = windex(lst)
			res_list.append(val)

		arr  =bytearray(res_list)
		binary_file.write(arr)


#Driver code
#try_probability_bytes(100)