

def inc(N):
    if N == 0:
        # print(1,end =" ") 
        return 
    inc(N-1)
    print(N,end =" ")

def dec(N):
    if N == 0:
        return 

    print(N,end =" ")
    dec(N-1)


import os 
os.system("clear")

# inc(5)
# dec(5)


def thrice_once(arr):
    # initialize ans
    #check the count of each bit
    # if ocunt is not divisibe by 3 that bit is set in the answer
    ans = 0

    for i in range(32):
        count = 0
        for j in range(len(arr)):
            if A[j] & (1 << i) > 0:
                count += 1
        
        if count %3 != 0:
            ans = ans | (1<<i)
    
    print(f"Value is {ans}")

A1 = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# thrice_once(A)

def find_two_only_once(A):
    # do XOR find the ans 
    # find the set bit 
    # Both elements will be different on the first set but , create two groups and 

    ans = 0
    for i in range(len(A)):
        ans = ans ^ A[i]
    
    for j in range(32):
        if ans & (1<<j) > 0:
            idx = j 
            break
    
    s , us = 0,0

    for i in range(len(A)):
        if A[i] & (1<<idx) > 0:
            s = s ^ A[i]
        else :
            us = us ^ A[i]
    print(s,us)
    
# A = [1, 2, 3, 1, 2, 4]
# find_two_only_once(A)


def check_plaindrome(str,s ,e):
    if s > e :
        return True
    
    if str[s] != str[e] :
        return False

    return check_plaindrome(str,s+1,e-1)

# print(check_plaindrome('radaar',0,4) )

def p_print(arr,idx):
    if idx == len(arr) :
        return 
    
    print(arr[idx],end = " ")
    p_print(arr, idx+1)

# p_print([1,2,3],0)


def find_all(arr, key , idx , count):
    if idx == len(arr):
        return [0]*count 

    if arr[idx] != key:
        return find_all(arr, key, idx+1 , count)
    
    if arr[idx] == key :
        A = find_all(arr, key, idx+1 , count+1)
        A[count] = idx
        return A

# print(find_all([1,2,1,4,1],1,0,0))
import os
os.system('clear')

def solve(A,B):
    es = [0]* len(A)
    es[0] = 1 if A[0] %2 ==0 else 0

    

    for i in range(1, len(A)):
        if A[i] %2 ==0 :
            es[i] = es[i-1] + 1 
        else :
            es[i] = es[i-1]
    
    print(es)

    res =[]
    for j in range(len(B)):
        L = B[j][0]
        R = B[j][1]

        if L == 0:
            ans = es[R]
        else :
            ans = es[R] - es[L-1]
        res.append(ans)
    
    print(res)





# A = [1,2,3,4]
# B = [[0,3],[2,3]]
# solve(A,B)


def solve(A):
    div_sum = [0] * len(A)

    div_sum[0] = 1 if A[0] % 4 == 0 or A[0] % 5 == 0 else 0
    
    for i in range(1, len(A)):
        if A[i] % 4 == 0 or A[i] % 5 == 0 :
            div_sum[i] = 1 
        else :
            div_sum[i] = 0

    print(div_sum)
    i , j = 0, 0 
    ans = 0

    for k in range(len(div_sum)):
        if A[k] == 1:
            j = j + 1
        else :
            j = j + 1
            i = j
            
            ans = max(ans, j-i+1)

        print(f"i ,  j : {i},{j}")
        
        print(ans)

# A = [4,1,10,15]
# A = [1,9,2]
# print(solve(A))


def solve(A, B):
    freq = {}
    res = []
    for num in A :
        if num not in freq :
            freq[num] = 1
        else :
            freq[num] += 1
    print(freq)
    print(freq)
    for val in B :
        if val in freq :
            res.append(freq[val])
        else :
            res.append(0)
    
    print(res)

# A = [2, 5, 9, 2, 8]
# B = [3, 2]
# solve(A,B)

def solve( A):
    temp = A.copy()
    
    print(temp)
    temp.sort()
    print(temp)



A = [10, 5, 3, 4, 3, 5, 6]
print(solve(A))

A =[1,2]
B = [2,3]
c = []

print(c)