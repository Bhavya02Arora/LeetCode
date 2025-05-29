from collections import defaultdict


def max_non_repeating_characters(s):
	dict = defaultdict()
	l = 0
	n = len(s)
	if not s:
		return 0
	if n == 1:
		return 1

	max_len = 1
	for r in range(n):
		if s[r] not in dict:
			dict[s[r]] = r
			max_len = max(max_len, r - l + 1)  # 2
		else:
			max_len = max(max_len, r - l)

			# gracefully removing l characters from dictionary
			while l < dict[s[r]]:
				del dict[s[l]]
				l += 1
			l = max(l, dict[s[r]] + 1)

			dict[s[r]] = r  # m = 2
			max_len = max(max_len, r - l)  # 0

	return max_len

s = "abcabc"
print(max_non_repeating_characters(s))
