#AoC Day3

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