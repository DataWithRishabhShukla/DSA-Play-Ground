
def subarray_with_sum(A,B):
    s , e = 0 , 0 
    n = len(A)
    sum = 0 
    count = 0
    while e < n:
        sum += A[e]
        
        while sum > B :
            sum -= A[s]
            s += 1
        if sum == B :
            print(f"Inside the sum == B")
            print(f"s,e :{s,e}")
            break 
        e += 1
    
    print(f"Value of the s , e : ")
    print(A[s:e+1])
    


arr =  [1, 2, 3, 4, 5]
B = 5
subarray_with_sum(arr,B)
