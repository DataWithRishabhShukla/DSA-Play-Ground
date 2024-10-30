def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")


def pivot_array(A):
    print(A)
    n = len(A)
    l , r = 1, n-1
    pivot = A[0]
    print(f"l,r : {l,r} {A[l],A[r]}")

    while l <= r:
        if A[l] <= pivot :
            l +=1
        elif A[r] > pivot :
            r -= 1
        else :
            print(f"swapping the elements :{A[l],A[r]} ")
            A[l],A[r] = A[r],A[l]
            l += 1
            r -= 1

    print(f"Array after swapping :{A}")

    print(f"\nCurrent value of the L, R :{l,r}")
    print(f"Values present in the index l,r are :{A[l],A[r]}")

    print(f"Swapping the values of pivot element with value :{r, A[r]}")
    A[0] , A[r] = A[r],A[0]
    print(f"\n\nFinal sorted array is :{A}\n")

start_new("Pivot Element Problem ")

arr = [54,26,93,17,77,31,44,55,20]
pivot_array(arr)
