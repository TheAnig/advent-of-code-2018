res = 0
freq = set()
notFound = True
with open('input.txt') as file:
	lines = file.readlines()
	while notFound:
		for line in lines:
			res += int(line)
			if res in freq:
				notFound = False
				print(res)
				break
			freq.add(res)