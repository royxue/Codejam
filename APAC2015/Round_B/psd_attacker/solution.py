from cj_input import cj_inputs
import math

total, data = cj_inputs("A-small-attempt3.in")

def psd_attacker(data):
	answer_list = []
	for i in data:
		answer = 0
		val_M = int(i[0])
		val_N = int(i[1])
		if val_M == val_N:
			answer = math.factorial(val_N)
		else:
			diff = (val_N - val_M)
			multi_1 = math.factorial(val_M)
			answer = (multi_1 * val_M * val_N)/(diff+1)+(multi_1) * (pow(val_M,diff)-val_M) * val_N/ math.factorial(diff)

		answer = answer%(1000000007)

		answer_list.append(answer)

	return answer_list

output_idx = 1
for i in psd_attacker(data):
	print "Case #%d: %d"%(output_idx, i)
	output_idx += 1