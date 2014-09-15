import re

pre_data = open("B-small-attempt1.in")

data_test = []
for i in pre_data:
	data_test.append(re.split(" ", i))

total = data_test.pop(0)

def order_check(data, idx, num, order):
	if 'left' in order:
		for x in range(idx+1, idx+num+1):
			for y in range(0, num-1):
				for i in range(1, num-y):
					if int(data[x][y+i]) != 0:
						if int(data[x][y]) == int(data[x][y+i]):
							data[x][y] = str(int(data[x][y]) + int(data[x][y+i]))
							data[x][y+i] = str(0) 
							break
						else:
							continue
	elif 'up' in order:
		for x in range(idx+1, idx+num):
			for y in range(num):
				for i in range(1, num-x+idx+1):
					if int(data[x+i][y]) != 0:
						if int(data[x][y]) == int(data[x+i][y]):
							data[x][y] = str(int(data[x][y]) + int(data[x+i][y]))
							data[x+i][y] = str(0) 
						break
					else:
						continue

	elif 'down' in order:
		for x in range(idx+num, idx+1, -1):
			for y in range(num):
				for i in range(1, x-idx):
					if int(data[x-i][y]) != 0:
						if int(data[x][y]) == int(data[x-i][y]):
							data[x][y] = str(int(data[x][y]) + int(data[x-i][y]))
							data[x-i][y] = str(0)
						break
					else:
						continue 
	elif 'right' in order:
		for x in range(idx+1, idx+num+1):
			for y in range(num-1, 0, -1):
				for i in range(1, y+1):
					if int(data[x][y-i]) != 0:
						if int(data[x][y]) == int(data[x][y-i]):
							data[x][y] = str(int(data[x][y]) + int(data[x][y-i]))
							data[x][y-i] = str(0)
						break
					else:
						continue
	return data[idx+1: idx+num+1]

def data_process(data, order):
	if 'left' in order:
		for x in range(0, len(data)):
			for y in range(len(data)-1):
				if int(data[x][y]) == 0:
					for i in range(1, len(data)-y):
						if int(data[x][y+i]) != 0:
							data[x][y] = data[x][y+i]
							data[x][y+i] = str(0) 
							break
						else:
							continue
	elif 'up' in order:
		for x in range(0, len(data)-1):
			for y in range(len(data)):
				if int(data[x][y]) == 0:
					for i in range(1, len(data)-x):
						if int(data[x+i][y]) != 0:
							data[x][y] = data[x+i][y]
							data[x+i][y] = str(0)
							break
						else:
							continue

	elif 'down' in order:
		for x in range(len(data)-1, 0, -1):
			for y in range(len(data)):
				if int(data[x][y]) == 0:
					for i in range(1, x+1):
						if int(data[x-i][y]) != 0:
							data[x][y] = data[x-i][y]
							data[x-i][y] = str(0) 
							break
						else:
							continue
	elif 'right' in order:
		for x in range(0, len(data)):
			for y in range(len(data)-1, 0, -1):
				if int(data[x][y]) == 0:
					for i in range(1, y+1):
						if int(data[x][y-i])!= 0:
							data[x][y] = data[x][y-i]
							data[x][y-i] = str(0)
							break
						else:
							continue
	return data

output_idx = 0
idx = 0
for line in data_test:
	if len(line) == 2:
		output_idx += 1
		num, order = int(line[0]), line[1]
		pre_answer = order_check(data_test, idx, num, order)
		answer = data_process(pre_answer, order)
		print "Case #%d:"%(output_idx)
		for i in answer:
			print " ".join(i)
		idx += num+1


