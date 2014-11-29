import re

def cj_inputs(file):
	""" transfer Codejam .in data file into list array

	Return [data number, data]
	"""
	raw_content = open(file)
	content = []
	for line in raw_content:
		new_line = re.split("\n*", line)
		if '' in new_line:
			new_line.remove('')
		content.append(new_line)

	num = content.pop(0)

	return num, content
	
# print cj_inputs("data2.in")