import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        # Min-heap priority queue
        pq = []
        heapq.heappush(pq, (0, S))  # (distance, node)

        # Distance array initialized to a large value
        dist = [float('inf')] * V
        dist[S] = 0

        while pq:
            dis, node = heapq.heappop(pq)

            for neighbor in adj[node]:
                adjNode, edgeWeight = neighbor
                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    heapq.heappush(pq, (dist[adjNode], adjNode))

        return dist


######## using set as priority queue ########
class Solution:
    def dijkstra(self, V, adj, S):
        # Set to act as a priority queue alternative
        active_nodes = set()

        # Distance array initialized to a large value
        dist = [float('inf')] * V
        dist[S] = 0

        active_nodes.add((0, S))  # (distance, node)

        while active_nodes:
            # Extract node with the smallest distance
            dis, node = min(active_nodes)  # This replaces the heap pop operation
            active_nodes.remove((dis, node))

            for neighbor in adj[node]:
                adjNode, edgeWeight = neighbor
                if dis + edgeWeight < dist[adjNode]:
                    # Remove the old distance if it exists in the set
                    if (dist[adjNode], adjNode) in active_nodes:
                        active_nodes.remove((dist[adjNode], adjNode))

                    dist[adjNode] = dis + edgeWeight
                    active_nodes.add((dist[adjNode], adjNode))

        return dist
