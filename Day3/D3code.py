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
				input_list.append(x)

input_list = []
integrate_input('D3input.txt')

test_cases = {
    (('Test 1',), ('R8','U5','L5','D3'), ('U7','R6','D4','L4')) : 6,
    (('Test 2',), ('R75','D30','R83','U83','L12','D49','R71','U7','L72'),
    ('U62','R66','U55','R34','D71','R55','D58','R83')) : 159,
    (('Test 3',), ('R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'),
    ('U98','R91','D20','R16','D67','R40','U7','R15','U6','R7')) : 135,
}

def tests(test_cases, function):
	"""
	Takes a number of test cases as key-value pairs.
	The key is the input and the value represents the expected output.

	Also takes a function to run the test cases on.
	"""
	for key in test_cases.keys():
		if function(key) == test_cases[key]:
			print ('Tested for {} and got {}, which is correct!'.format(key[0][0], test_cases[key]))
		else:
			print ('-------------------------------------------------------')
			print ('ISSUE with {}'.format(key[0][0]))
			print ('Expected {} and instead got {}!'.format(test_cases[key], function(key)))
			print ('-------------------------------------------------------')

def manhattan_distance(input):
    """
    Takes a tuple of 3 tuples - Test case, first and second wire
    """
    assert type(input) == tuple
    for x in range(len(input)):
        assert type(input[x]) == tuple

    wire1 = input[1]
    wire2 = input[2]

    def make_path(wire):
        wire_path = [(0,0),]
        for step in wire:
            if step[0] == 'R':
                wire_path.append((wire_path[-1][0], wire_path[-1][1] + int(step[1:])))
            elif step[0] == 'L':
                wire_path.append((wire_path[-1][0], wire_path[-1][1] - int(step[1:])))
            elif step[0] == 'U':
                wire_path.append((wire_path[-1][0] + int(step[1:]), wire_path[-1][1]))
            elif step[0] == 'D':
                wire_path.append((wire_path[-1][0] - int(step[1:]), wire_path[-1][1]))
        return wire_path

    wire1_path = make_path(wire1)
    wire2_path = make_path(wire2)

    def find_crossings(path1, path2):
        pass

    return (wire1_path, wire2_path)


n = (('Test 1',), ('R8','U5','L5','D3'), ('U7','R6','D4','L4'))

w1, w2 = manhattan_distance(n)
print (w1)
print (w2)
#tests(test_cases, manhattan_distance)