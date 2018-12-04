import re
import numpy


with open('day_3.in') as f:
	allClaims = [re.findall(r"[\w']+", (line.strip())) for line in f]


def claim(allClaims):
	mat = numpy.zeros((1500, 1500))
	for claim in allClaims:
		print(claim)
		pos_x = int(claim[1])
		pos_y = int(claim[2])
		dimension = claim[3].split('x')
		wide = int(dimension[0])
		tall = int(dimension[1])
		for i in range(pos_x, pos_x + wide):
			for j in range(pos_y, pos_y + tall):
				mat[i][j] += 1
	return mat

def overlapCount(mat):
	count = 0
	for i in range(1500):
		for j in range(1500):
			if mat[i][j] > 1:
				count += 1
	return count

mat = claim(allClaims)
print (overlapCount(mat))

def test(test_case):
	allClaims = [re.findall(r"[\w']+", (line.strip())) for line in test_case]
	mat = claim(allClaims)
	return overlapCount(mat)

TEST_1 = [
	'#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2'
]

assert test(TEST_1) == 4
