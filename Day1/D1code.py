# AoC 2019 -- Day 1

def integrate_input(input_file):
	"""
	Takes the daily input file and adds it to a list
	"""
	with open(input_file, 'r') as f:
		for line in f:
			input_list.append(int(line))

input_list = []
integrate_input('D1input.txt')

test_cases = {12: 2, 14: 2, 1969: 654, 100756: 33583}

def tests(test_cases, function):
	"""
	Takes a number of test cases as key-value pairs.
	The key is the input and the value represents the expected output.

	Also takes a function to run the test cases on.
	"""
	for key in test_cases.keys():
		if function(key) == test_cases[key]:
			print ('Tested for value {} and got {}, which is correct!'.format(key, test_cases[key]))
		else:
			print ('Issue with the test for value {}'.format(key))
			print ('Expected {} and instead got {}!'.format(test_cases[key], fuel_calculation(key)))


def fuel_calculation(mass):
	return (mass // 3) - 2

incremented_total = 0

for element in input_list:
	incremented_total += fuel_calculation(element)

print (incremented_total)

tests(test_cases, fuel_calculation)