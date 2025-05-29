from heapq import *


def manage_heap(index, pq):
	while pq and pq[0][1] < index:
		heappop(pq)
	if pq:
		return pq[0][0]
	else:
		return 0
def maximumRobots(chargeTimes, runningCosts, budget):

	max_k = 0
	sliding_window_sum = 0
	n = len(chargeTimes)
	j = 0
	pq = []
	heapify(pq)

	for i in range(1, n):
		sliding_window_sum += runningCosts[i]
		heappush(pq, (-chargeTimes[i], i))

		while (-1 * manage_heap(j, pq) + ((i - j +1) * sliding_window_sum)) > budget:
			# remove from heap
			sliding_window_sum -= runningCosts[j]
			j += 1
		max_k = max(i - j +1, max_k)
	return max_k


chargeTimes = [3,6,1,3,4]
runningCosts = [2,1,3,4,5]
budget = 25
print(maximumRobots(chargeTimes, runningCosts, budget))