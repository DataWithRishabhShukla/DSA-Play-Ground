

def insert_into_heap(arr, node):
    # Insert the node to the heap
    print(f"Processing for {node=}") 
    arr.append(node)
    i = len(arr) - 1 # we will start from the leaf node 
    print(f"Pre Swap : {arr=}")
    while i > 0 and arr[i] < arr[(i-1)//2] :
        arr[i] , arr[(i-1)//2] = arr[(i-1)//2] , arr[i]
        i = (i-1)//2
    print(f"Post Swap : {arr=} \n")
    

    

def solve(A):
    ans = []
    for node in A :
        insert_into_heap(ans,node)
    
    print(f"{ans = }")
    

A = [5, 13, -2, 11, 27, 31, 0, 19]
solve(A)