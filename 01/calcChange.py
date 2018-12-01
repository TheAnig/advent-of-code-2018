res = 0
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		res += int(line)

print(res)