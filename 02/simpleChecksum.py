def checkN(st, n):
	d = {}
	for c in st:
		d[c] = d.get(c, 0) + 1

	return len([k for k,v in d.items() if v == n]) > 0

two = 0
three = 0
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		two += 1 if checkN(line, 2) else 0
		three += 1 if checkN(line, 3) else 0

print(two*three)