s= "wxyz"


result = 0
for i in s:
	if i == 's' or i == 'z':
		result += 4
		continue

	pos = ord(i)+1 - ord('a')
	if ord(i) > ord('s'):
		pos -= 1
	# divide the position by 3
	div = pos/3
	# extract the first decimal part of the division
	first_decimal = int((div *10 )%10)
	if first_decimal == 3:
		result += 1
	elif first_decimal == 6:
		result += 2
	else:
		result += 3
print(result)



