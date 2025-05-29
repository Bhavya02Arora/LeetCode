import heapq


def dijkstra(graph, S, D):
	"""
	Finds the shortest path from source (S) to destination (D) using Dijkstra's algorithm.

	:param graph: Adjacency list where graph[u] = [(v, weight), ...] represents edges.
	:param S: Source node.
	:param D: Destination node.
	:return: Tuple (min_distance, path)
	"""
	# Step 1: Initialize distance and parent dictionaries
	dist = {node: float('inf') for node in graph}  # Distance from S to each node
	parent = {node: None for node in graph}  # Parent tracking for path reconstruction
	dist[S] = 0  # Distance from S to itself is 0

	# Min-Heap (Priority Queue) - stores (distance, node)
	pq = [(0, S)]

	while pq:
		d, u = heapq.heappop(pq)  # Extract node with min distance

		if u == D:  # Stop early if we reach the destination
			break

		for v, weight in graph[u]:  # Explore neighbors
			if dist[u] + weight < dist[v]:  # Relaxation
				dist[v] = dist[u] + weight
				parent[v] = u
				heapq.heappush(pq, (dist[v], v))

	# Step 3: Reconstruct the shortest path from S to D
	path = []
	node = D
	while node is not None:
		path.append(node)
		node = parent[node]

	path.reverse()  # Reverse to get path from S to D

	return dist[D], path if dist[D] != float('inf') else (float('inf'), [])  # If no path exists


# Example Graph (Adjacency List)
graph = {
	'A': [('B', 1), ('C', 4)],
	'B': [('A', 1), ('C', 2), ('D', 5)],
	'C': [('A', 4), ('B', 2), ('D', 1)],
	'D': [('B', 5), ('C', 1)]
}

# Find shortest path from 'A' to 'D'
min_distance, path = dijkstra(graph, 'A', 'D')
print(f"Minimum Distance: {min_distance}")
print(f"Shortest Path: {path}")
