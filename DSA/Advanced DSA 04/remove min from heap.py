def insert_into_heap(arr, node):
    # Insert the node to the heap
    
    arr.append(node)
    i = len(arr) - 1 # we will start from the leaf node 
    
    while i > 0 and arr[i] < arr[(i-1)//2] :
        arr[i] , arr[(i-1)//2] = arr[(i-1)//2] , arr[i]
        i = (i-1)//2


def remove_min_ele_from_heap(arr):

    if len(arr) == 0:
        return -1

    # swap the first(root) with last node 
    n = len(arr)
    arr[0] ,arr[n-1] = arr[n-1],arr[0]

    removed_ele = arr.pop()

    i = 0 
    while 2*i+1 < len(arr) :
        min_idx = 2*i + 1
        if 2*i + 2 < len(arr) and arr[2*i+2] < arr[min_idx] :
            min_idx = 2*i + 2

        if arr[i] <= arr[min_idx]:
            break
        
        arr[i] , arr[min_idx] =arr[min_idx] ,arr[i]
        i  = min_idx
    return removed_ele

ans = []
del_ele_list = []
A = [[2,3],[1,-1],[1,-1],[1,-1],[1,-1],[2,9],[2,17],[1,-1],[2,13]]

for op in A :
    print(f"\n\nProcessing for the {op=}")
    if op[0] == 2 :
        print(f"heap pre insert     {ans=}")
        insert_into_heap(ans,op[1])
        print(f"heap post insert    {ans=}")
    elif op[0] == 1 :
        print(f"deleted element list before {del_ele_list}")
        d_ele = remove_min_ele_from_heap(ans)
        print(f"{d_ele=}")
        del_ele_list.append(d_ele)
        print(f"deleted element list after {del_ele_list}")


print(f"{del_ele_list=}")


