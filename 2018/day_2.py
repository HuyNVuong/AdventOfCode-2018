
with open('day_2.in') as f:
	allString = [line.strip() for line in f]

"""
Part 1
"""
def checkSum(allString):
	count_2 = 0
	count_3 = 0
	for string in allString:
		count_3_flag = 0
		count_2_flag = 0
		stringSet = ''.join(set(string))
		for c in stringSet:
			if string.count(c) == 3:
				count_3_flag = 1
			if string.count(c) == 2:
				count_2_flag = 1
		if count_3_flag == 1:
			count_3 += 1
		if count_2_flag == 1:
			count_2 += 1
	return count_2 * count_3

print (checkSum(allString))

""" 
Unit testing
"""
assert checkSum(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12

