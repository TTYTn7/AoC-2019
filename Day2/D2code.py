# AoC 2019 -- Day 2 - Intcode Computer

# Part 1 ---------------------------------------------------

def integrate_input(input_file):
	"""
	Takes the daily input file and adds it to a list
	"""
	with open(input_file, 'r') as f:
		for element in f:
			element = element.split(',')
			for x in element:
				input_list.append(int(x))

input_list = []
integrate_input('D2input.txt')

print (input_list)

test_cases = {  (1,9,10,3,2,3,11,0,99,30,40,50):[3500,9,10,70,2,3,11,0,99,30,40,50],
				(1, 0, 0, 0, 99): [2, 0, 0, 0, 99],
				(2, 3, 0, 3, 99): [2, 3, 0, 6, 99],
				(2, 4, 4, 5, 99, 0): [2, 4, 4, 5, 99, 9801],
				(1, 1, 1, 4, 99, 5, 6, 0, 99): [30, 1, 1, 4, 2, 5, 6, 0, 99],
				}

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
			print ('-------------------------------------------------------')
			print ('ISSUE with the test for value {}'.format(key))
			print ('Expected {} and instead got {}!'.format(test_cases[key], function(key)))
			print ('-------------------------------------------------------')

def intcode_computer(code):
	if type(code) == tuple:
		code = list(code)
	c_index = 0
	while True:
		if code[c_index] == 99:
			return code
		elif code[c_index] == 1:
			code[code[c_index + 3]] = code[code[c_index + 1]] + code[code[c_index + 2]]
		elif code[c_index] == 2:
			code[code[c_index + 3]] = code[code[c_index + 1]] * code[code[c_index + 2]]
		else:
			return 'Error, unknown opcode! Received {} while expecting either 1, 2, or 99!'.format(code[current_index])
		c_index += 4

#tests(test_cases, intcode_computer)
input_list[1] = 12
input_list[2] = 2
answer = intcode_computer(input_list)
print (answer[0])

# Part 2 -------------------------------------------------------------

#test_cases_p2 = {12: 2, 14: 2, 1969: 966, 100756: 50346}



#tests(test_cases_p2, fuel_calculation_p2)


