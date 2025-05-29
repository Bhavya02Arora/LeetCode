import heapq as hq
import math


class Solution:

	# Function to return the minimum cost to react at bottom
	# right cell from top left cell.

	# Function to check if cell indexes are within bounds.
	def isValid(self, x, y, n):
		return (x >= 0 and x < n and y >= 0 and y < n)

	def minimumCostPath(self, grid):
		# Code here

		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		n = len(grid)
		s = (0, 0)
		li = []
		dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

		dp[0][0] = grid[0][0]

		hq.heappush(li, (dp[0][0], s))

		while len(li):
			dp_val, co_ords = hq.heappop(li)

			if dp_val != dp[co_ords[0]][co_ords[1]]:
				continue

			for dir in directions:
				x = co_ords[0] + dir[0]
				y = co_ords[1] + dir[1]

				if self.isValid(x, y, n) and (dp[x][y] > dp_val + grid[x][y]):
					dp[x][y] = dp_val + grid[x][y]

					hq.heappush(li, (dp[x][y], (x, y)))

		return dp[n - 1][n - 1]

s = Solution()
grid = [[31, 100, 65, 12, 18],
		[10, 13, 47, 157, 6],
		[100, 113, 174, 11, 33],
		[88, 124, 41, 20, 140],
		[99, 32, 111, 41, 20]]
print(s.minimumCostPath(grid))
# Output: 327
