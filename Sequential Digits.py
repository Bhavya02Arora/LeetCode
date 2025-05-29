import math

def sequentialDigits(low: int, high: int):
	low_len = len(str(low))
	high_len = len(str(high))
	extreme_left = low // int(math.pow(10, low_len - 1))
	print(extreme_left)
	ans = []

	for start in range(extreme_left, 9):
		next_number = (start + 1)
		if start == 7:
			print(next_number)
		while start <= high:
			n = (start * 10) + ((next_number))  # 78
			start = n  # 78
			next_number += 1
			# print(start)
			if low < start <= high:
				ans.append(start)
			if next_number > 9:
				break
	print(ans)
	return ans

sequentialDigits(1000, 13000)

