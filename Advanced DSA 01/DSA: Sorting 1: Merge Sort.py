
def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")


def merge_Sort(A,B):
    print(A,B)
    n ,m = len(A) , len(B)
    res = [0] * (n+m)
    print(res)

    i,j,k = 0,0,0
    # using two pointers approach
    while i < n and j < m:
        if A[i] <= B[j]:
            res[k] = A[i]
            i += 1
            k += 1
        else :
            res[k] = B[j]
            k += 1
            j += 1
    
    while i < n :
        res[k] = A[i]
        i += 1
        k += 1
    
    while j < m :
        res[k] = B[j]
        k += 1
        j += 1
    
    print(f"Merger sorted array is : {res}")



start_new("Merge sort !!!")

A = [2,4,7,8,12]
B = [3,5,6,7]
merge_Sort(A,B)
