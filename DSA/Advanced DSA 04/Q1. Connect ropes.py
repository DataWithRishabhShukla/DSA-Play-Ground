from queue import PriorityQueue
# from common.common_library import clear_terminal


def connect_ropes(A):
    pq = PriorityQueue()
    for rope in A :
        pq.put(rope)
    
    print(pq)
    print(type(pq))

    
    print(f"len before the pop :{pq.qsize()= }")
    smallest = pq.get()
    print(f"{smallest = }")
    print(f"len after the pop :{pq.qsize()= }")


# clear_terminal()
A = [5, 17, 100, 11]
connect_ropes(A)
