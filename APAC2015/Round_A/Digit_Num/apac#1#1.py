import re

digit_num = {0:[1111110], 1:[0110000], 2:1101101, 3:1111001, 4:0110011, 5:1011011, 6:1011111, 7:1110000, 8:1111111, 9:1111011}

data = open("data.in")
test_data = []
for i in data:
	test_data.append(re.split(" ", i))

def check_good(list):
	

print list(test_data[1][1])
	