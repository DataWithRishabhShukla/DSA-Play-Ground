

from queue import PriorityQueue
def get_ath_largest(arr, A):
    pq = PriorityQueue()
    ans = []

    for i in range(len(arr)):
        pq.put(arr[i])

        if pq.qsize()  < A :
            ans.append(-1)
        else :
            if pq.qsize() > A :
                pq.get()
            ans.append(pq.queue[0])
            
        
    print(f"{ans=}")



A = 2
B = [15, 20, 99, 1]

get_ath_largest(B,A)