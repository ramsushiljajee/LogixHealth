from sys import maxsize

def sameElementAdjacent(string):
	n = len(string)
	str_set = set()
	str_set.add(string[0])

	for i in range(1, n):
		if string[i] == string[i - 1]:
			continue
		
		if string[i] in str_set:
			return False

		str_set.add(string[i])
	return True

def minmumSwaps(string, l, r, count, minmum):

	if l == r:
		if sameElementAdjacent(string):
			return count
		else:
			return maxsize

	for i in range(l + 1, r + 1, 1):
		temp = string[i]
		string[i] = string[l]
		string[l] = temp
		count += 1

		a = minmumSwaps(string, l + 1, r, count, minmum)

		temp = string[i]
		string[i] = string[l]
		string[l] = temp
		count -= 1

		b = minmumSwaps(string, l + 1, r, count, minmum)

		minmum = min(minmum, min(a, b))

	return minmum

n = int(input())
for i in range(n):
    string = input()
    string = list(string)
    str_n = len(string)

    count = 0
    minmum = maxsize
    print(minmumSwaps(string, 0, str_n - 1, count, minmum))
