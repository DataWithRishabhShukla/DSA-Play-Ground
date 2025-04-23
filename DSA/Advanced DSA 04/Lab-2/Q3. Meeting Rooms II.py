
from queue import PriorityQueue
def solve(A, B):
    from queue import PriorityQueue
    sort_b = sorted(B,key = lambda x:x[0])
    pq = PriorityQueue()
    print(sort_b)
    pq.put(sort_b[0][1]) # first room will be needed for first meeting 

    
    for x in range(1,A):
        start_time = sort_b[x][0]
        end_time  = sort_b[x][1]

        if start_time >= pq.queue[0] :
            pq.get()

        pq.put(end_time)

        
    print(f"Meeting room needed :{pq.qsize()}")


A = 3
B = [ [0, 30],
      [5, 10],
      [15, 20] ]


solve(A,B)

