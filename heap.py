import heapq

pq = []
heapq.heappush(pq, 10)
heapq.heappush(pq, 1)
heapq.heappush(pq, 5)

x = heapq.heappop(pq)
print(x)
print(pq)
