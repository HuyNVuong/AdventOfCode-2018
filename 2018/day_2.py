
with open('day_2.in') as f:
	allString = [line.strip() for line in f]

"""
Part 1. Find sum of counts 2 and counts 3 of string
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
Part 2. Find 2 string missing by exactly 1 character (should be)
Answer: efmyhuckqldtwjyvisipargno
"""
def stringDiff(str1, str2):
	# We only want to return 1 character
	count = 0
	for i in range(len(str1)):
		if (str1[i] != str2[i]):
			index_to_pop = i
			count += 1
			if count > 1:
				return -1
	return index_to_pop

def checkCommon(allString):
	minPair = ""
	minArray = []
	solution = []
	for i in range(len(allString) - 1):
		s1 = set(allString[i])
		for j in range(i + 1, len(allString)):
			index_to_pop = stringDiff(allString[i], allString[j])
			if index_to_pop != -1:
				solution = [c for c in allString[j]]
				solution.pop(index_to_pop)
				return ''.join(solution)


print (checkCommon(allString))

"""
Unit testing
"""
assert checkSum(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12
assert checkCommon(['abcde', 'fghij','klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'
