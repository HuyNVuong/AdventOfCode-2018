total = 0

"""
part 1
"""
with open('day_1.in') as f:
	numbers = [int(line.strip()) for line in f]
print (sum(numbers))
""" 
part 2
"""
def allFreq(numbers, start: int = 0):
	currSum = 0
	while (True):
		for n in numbers:
			yield currSum
			currSum += n
			
def firstRepeatFreq(numbers):
	seen = set()
	for f in allFreq(numbers, 0):
		if f in seen:
			return f
		else:
			seen.add(f)
	
print(firstRepeatFreq(numbers))

"""
Unit testing
"""			
assert firstRepeatFreq([1, -1]) == 0
assert firstRepeatFreq([3, 3, 4, -2, -4]) == 10