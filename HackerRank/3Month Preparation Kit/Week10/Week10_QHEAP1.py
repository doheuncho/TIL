# Enter your code here. Read input from STDIN. Print output to STDOUT
from heapq import heappush, heappop

Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input())


def qheap1(queries):
    heap = []
    removed = set()
    
    for query in queries:
        if query[0] == '3':
            while True:
                if heap[0] in removed:
                    heappop(heap)
                else:
                    yield heap[0]
                    break
        else:
            q, v = query.split()
            v = int(v)
            if q == '1':
                heappush(heap, v)
                removed.discard(v)
            elif q == '2':
                removed.add(v)


result = qheap1(queries)
for res in result:
    print(res)
