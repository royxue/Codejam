import re


# data pre processing
input_file = open("A-small-practice.in")
data = []

for i in input_file:
	data.append(re.split(" ", i))

data.remove(data[0])

bound = 0
idx = 0
line_idx = 0

def check_line(line):
	checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in line:
		check_p = int(i)
		if check_p in checker:
			checker.remove(check_p)
		else:
			return False
	return True

for i in data:
	if bound == 0:
		bound = pow(int(i[0]),2)
		idx += 1
	else:
		line = ((idx-1) * bound)+1
		print line
		max_num = bound + 1
		for nm in range(max_num):
			print check_line(data[idx+nm])
		bound = 0



		continue

