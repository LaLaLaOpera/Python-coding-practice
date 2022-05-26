import heapq 

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    answer =0
    while True:
        if len(heap) <= 1:
            return -1
        else:
            answer +=1
            newNum = heapq.heappop(heap)+heapq.heappop(heap)*2
            heapq.heappush(heap,newNum)
            if heap[0]>=K:
                return answer
