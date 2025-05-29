"""Problem: Analyze User Website Visit Pattern
Difficulty: Medium

Topics: Array, Hash Table

You are given three arrays: username, timestamp, and website of the same length n, where the i-th tuple (username[i], timestamp[i], website[i]) indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct). A user is said to follow a pattern if they visited those three websites in the exact order specified by the pattern, regardless of the timestamps (though the visits must be in chronological order).

Your task is to find the most common 3-sequence pattern among all users. Specifically:

For each user, identify all possible 3-sequences of websites they visited (in chronological order).
Among all such 3-sequences across all users, find the one that appears the most times.
If there are multiple patterns with the same maximum frequency, return the lexicographically smallest one.
Return the most common 3-sequence as a list of strings.

Input:
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

Output: ["home","about","career"]

Explanation:
- Joe visited: ["home","about","career"] (times 1-2-3)
- James visited: ["home","cart","maps","home"] (times 4-5-6-7), giving sequences like ["home","cart","maps"], ["cart","maps","home"]
- Mary visited: ["home","about","career"] (times 8-9-10)
The 3-sequence "home","about","career" appears twice (Joe and Mary).
No other 3-sequence appears more than once.
Thus, ["home","about","career"] is the answer.

"""
from collections import defaultdict
from itertools import combinations
from typing import List

# Input
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]


# Input:
username = ["ua","ua","ua","ub","ub","ub"]
timestamp = [1,2,3,4,5,6]
website = ["a","b","a","a","b","c"]

d = defaultdict(list)

for _, uname, website in sorted(zip(timestamp, username,  website)):
	d[uname].append(website)

print(d)

count_dict = defaultdict(int)
for user, websites in d.items():
	for pattern in set(combinations(websites, 3)):
		count_dict[pattern] += 1

# purpose of below code is to print all possible 3-sequence pattern among all users
print(set(combinations(username, 3)))

# purpose of below code is to find the most common 3-sequence pattern among all users
# the below code is not giving correct output

most_repeated_pattern = max(count_dict, key=lambda x: (count_dict[x], x))

print(most_repeated_pattern)
most_repeated_pattern = ()
max_count = 0
# print("abc" < "def")
for k, v in count_dict.items():
	if v > max_count or (v == max_count and k < most_repeated_pattern):
		most_repeated_pattern = k
		max_count = v

print(most_repeated_pattern)




