def dist(s1, s2):
	diff = 0
	for i in range(0, len(s1)):
		if s1[i] != s2[i]:
			diff += 1

	return diff

def getCommon(s1, s2):
	s = ""
	for i in range(0, len(s1)):
		if s1[i] == s2[i]:
			s+= s1[i]

	return s

s1 = ""
s2 = ""
with open('input.txt') as f:
	lines = f.readlines()
	for line1 in lines:
		for line2 in lines:
			if dist(line1, line2) == 1:
				s1 = line1
				s2 = line2

print(getCommon(s1, s2))