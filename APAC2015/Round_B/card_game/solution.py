from cj_input import cj_inputs

total, data = cj_inputs("C-large.in")

def list_remove(raw_list, diff):
	for a in range(len(raw_list)-2):
		a = (a)%len(raw_list)
		b = (a+1)%len(raw_list)
		c = (a+2)%len(raw_list)
		if len(raw_list) > 2:
			if abs(int(raw_list[a]) - int(raw_list[b])) == int(diff):
				if abs(int(raw_list[b]) - int(raw_list[c])) == int(diff):
					raw_list.remove(raw_list[a])
					a = (a)%len(raw_list)
					raw_list.remove(raw_list[a])
					a = (a)%len(raw_list)
					raw_list.remove(raw_list[a])
					return True

def card_game(data):
	idx = 0
	answer = []
	for i in range(idx, len(data), 2):
		diff = data[i][1]
		raw_list = data[i+1]
		for tn in range(len(raw_list)):
			if list_remove(raw_list, diff):
				continue
			else:
				break
		answer.append(len(raw_list))
	return answer

output_idx = 1
for i in card_game(data):
	print "Case #%d: %d"%(output_idx, i)
	output_idx += 1


