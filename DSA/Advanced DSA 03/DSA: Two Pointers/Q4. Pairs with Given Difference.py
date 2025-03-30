

def pair_with_diff(A,B):
    n = len(A)
    print(f"Before sorting :{A}")
    A.sort()

    s, e = 0 , 1

    while e < n:
        diff = A[e]- A[s]

        if diff > B :
            



    print(f"After sorting :{A}")


A = [8, 12, 16, 4, 0, 20]
pair_with_diff(A,3)