
def give_nom_of_bit(num):
    print(f"decimal rep :{num}")
    count = 0
    while num > 0:
        if num & 1 > 0:
            count +=1
        
        num = num >> 1
    
    return count


# print(give_nom_of_bit(11))


def solve(A):
    cnt = 0
    while A > 0:
        if (A & 1) > 0:
            cnt += 1
            A = A - 1 
        else :
            A = A >> 1
    
    print(f"Number of times help taken  :{cnt}")


solve(7)


def max_sum_sub_array(arr):
    max_sum = 0

    for i in range(len(arr)):
        sum1 = 0
        for j in range(i,len(arr)):
            sum1 += arr[j]
            max_sum = max(max_sum,sum1)
    
    print(f"max_sum is {max_sum}")

# max_sum_sub_array([1,2,3])

# max_sum_sub_array([-3,2,4,-1,3,-4,3])


def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")
    

def first_non_repaeating_ele(arr):
    freq  = {}
    for num in arr :
        if num in freq :
            freq[num] += 1
        else :
            freq[num] = 1
    
    for num in arr :
        if freq[num] == 1:
            return num 
    
    return -1 

arr = [4,3,3,2,5,6,4,5]
start_new("first_non_repaeating_ele")
print(first_non_repaeating_ele(arr) )


def print_all_subarry(arr):
    n = len(arr)
    for si in range(n):
        for ei in range(si,n):
            #print(f"value os si ei : {si,ei}")
            for k in range(si,ei+1):
                print(arr[k])
            
            print()



def solve(arr,B):

    count = 0 
    hs = {}
    for num in arr :

        right_pair = num - B
        left_pair = num + B
        if  right_pair in hs :
            count = count + hs[right_pair]
        
        if  left_pair in hs :
            count = count + hs[left_pair]
        
        if num in hs :
            hs[num] += 1
        else :
            hs[num] = 1

    return count 


start_new("a[i] - a[j] = B")
arr = [1, 2, 1, 2]
B = 1
print(solve(arr, B))


start_new("printing_all_subarray")
arr = [1,2,3]
print_all_subarry(arr)



def subarray_with_sum_b(A,B):
    n = len(A)
    psum = [0] * n
    psum[0] = A[0]
    print(psum)
    for i in range(1,n):
        psum[i] = psum[i-1] + A[i]

    print(psum)
    cnt = 0
    hm = {}
    for num in psum:
        if num == B :
            cnt += 1  
        
        if num - B in hm :
            cnt += hm[num-B]

        if num in hm :
            hm[num] += 1
        else :
            hm[num] = 1
    
    print( cnt)
 
start_new("printing_all_subarray_withsum_B")
A = [1, 0, 1]
B = 1

A = [0, 0, 0]
B = 0
subarray_with_sum_b(A,B)



def longest_subsrray_withsum_zero(A):
    n = len(A)

    psum = [0] * n
    psum[0] = A[0]

    for i in range(1,n):
        psum[i] = psum[i-1] + A[i]
    
    print(A)
    print(psum)
    ans = 0
    hm = {}
    for j in range(n) :
        print(hm)
        if psum[j] == 0:
            ans = max(ans,j+1)
        
        if psum[j] in hm :
            print("Inside the if psum[j] exist ")
            print(f"Pre ans , j :{ans, j}")
            ans = max(ans,j- hm[psum[j]] )
            print(f"post ans , j :{ans, j}")
        else :
            hm[psum[j]] = j
    print(f"Maximum length is : {ans}")



start_new("Longest Subarray Zero Sum")

A = [1, -2, 1, 2]
A = [3, 2, -1]
A = [1, -2, 1, 2]
A = [9,-20,-11,-8,-4,2,-12,14,1]
A = [-16,16,1]
longest_subsrray_withsum_zero(A)



def distinct_number_in_window(A,B):
    hm = {}
    res = []

    for i in range(B):
        if A[i] in hm :
            hm[A[i]]    += 1
        else :
            hm[A[i]]    = 1 

    res.append(len(hm))

    for j in range(B,len(A)):
        out_ele = A[j-B]
        if hm[out_ele] == 1 :
            del hm[out_ele]
        else :
            hm[out_ele] -= 1
        
        in_ele = A[j]
        if in_ele in hm :
            hm[in_ele]    += 1           
        else :
            hm[in_ele]    = 1
        
        res.append(len(hm))
    
    print(res)

     

start_new("Distinct Numbers in Window")

A = [1, 2, 1, 3, 4, 3]
B = 3
distinct_number_in_window(A,B)



start_new("Max Sum Contiguous Subarray")

def max_sum_subarray(A):
    csum = 0
    msum = float("-inf")

    for num in A:
        csum += num 
        msum = max(msum , csum)

        if csum < 0:
            csum = 0
    
    print(f"max possible sum is :{msum}")

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
max_sum_subarray(A)


def rain_water_trapped(A):
    # get the max on the both left and right 
    # Get the min of min(letf_max, right_max) - A[i]
    # if prev step answer > 0 , add to final answer 

    n = len(A)
    print()
    l_max,r_max = [0]*n , [0]* n
    l_max[0] = A[0]

    for i in range(1,n):
        l_max[i] = max(l_max[i-1] , A[i])
    print(f"Array is :{A}")
    print(f"Left max array is : {l_max}")

 
    r_max[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        r_max[i] = max(r_max[i+1] , A[i])
    
    print(f"Right max array is : {r_max}")
    ans = 0
    for i in range(1,n-1):
        water = min(l_max[i],r_max[i]) - A[i]
        if water > 0 :
            ans += water
    
    print(f"Final answer is {ans}")



start_new("Rain Water Trapped")
A = [5, 4, 1, 4, 3, 2, 7]
rain_water_trapped(A)


def continuous_sum_query(A,B):
    n = A
    ans = [0] * n

    for i in range(len(B)):
        si = B[i][0] - 1
        ei = B[i][1]

        amt = B[i][2]
        print(f"si, ei , amt :{si, ei , amt}")
        ans[si] += amt

        if ei  < n :
            ans[ei] -= amt
        print(ans)
        print()
    
    print(ans)

    # generating the prefix sum 
    for j in range(1,len(ans)):
        ans[j] = ans[j-1] + ans[j]
    
    print(ans)

start_new("Continuous Sum Query")
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
continuous_sum_query(A,B)


def print_boundry_selemts(arr):
    i , j = 0 , 0 
    n = len(arr)

    # printing the first row 
    for idx in range(1,n):
        print(arr[i][j] , end = " ")
        j += 1
    
    # printing last cols element 
    for idx in range(1,n):
        print(arr[i][j] , end = " ")
        i = i+1

    # printing last row element 
    for idx in range(1,n):
        print(arr[i][j], end = " ")
        j = j -1 

    # printing the first cols values 
    for idx in range(1,n):
        print(arr[i][j],end = " ")
        i = i -1
    
    

start_new("Print Boundry Elements")

A = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print_boundry_selemts(A)
print()


def print_spiral_matrix(arr):
    r, c = 0,0
    n = len(arr)
    #print(f"r,c,n : {r,c,n}")

    while r <= n and c <= n :
        print(f"\nr,c,n : {r,c,n}")
        print("Inside the loop !!!\n")
        
        for idx in range(1,n):
            print(arr[r][c],end = " ")
            c += 1

        for idx in range(1,n):
            print(arr[r][c],end = " ")
            r += 1

        for idx in range(1,n):
            print(arr[r][c],end = " ")
            c -= 1
        
        for idx in range(1,n):
            print(arr[r][c],end = " ")
            r -= 1
        
        r += 1
        c += 1
        n -= 2
    
    if n == 1 :
        print("Inside the if block")
        print(arr[r][c])

start_new("Print Spiral Matrix Elements")

A = [[1,2,3,4,5,6,7], [8,9,10,11,12,13,14], [15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42],[43,44,45,46,47,48,49]]

"""
[01,02,03,04,05,06,07]
[08,09,10,11,12,13,14]
[15,16,17,18,19,20,21]
[22,23,24,25,26,27,28]
[29,30,31,32,33,34,35]
[36,37,38,39,40,41,42]
[43,44,45,46,47,48,49]
"""
print_spiral_matrix(A)


def find_missing_number(arr):
    n = len(arr)
    print(f"Array before the replacing -ve,0 number :{arr}")
    for i in range(n):
        if arr[i] <= 0 :
            arr[i] = n+2
    
    print(f"Array after the replacing -ve,0 number  :{arr}")

    # marking the index 
    for i in range(n):
        ele = abs(arr[i])
        if ele <= n and ele >= 1:
            arr[ele-1] = -1 * abs(arr[ele-1])
    print(f"Array after the marking index  :{arr}")
    # Checking for the missing number 
    for i in range(n):
        if arr[i] > 0:
            print(f"Missing number is :{i+1}")
            break
    
    print(f"Missing number is :{n+1}")
    




start_new("Find the first missing natural number !!!")
A = [3, 4, -1, 1]
A = [1, 2, 0]
A= [-8, -7, -6]
find_missing_number(A)

def merge_sroted_intervals(arr):
    n = len(arr)
    start = arr[0][0]
    end = arr[0][1]
    res = []
    print(f"First start and end are : {start , end }")

    for i in range(1,n):
        curr_start = arr[i][0]
        curr_end = arr[i][1]
        print(f"Processing for : {curr_start,curr_end}")

        if curr_start <= end :
            start = min(curr_start,start)
            end = max(curr_end,end)
        else:
            res.append([start,end])
            start = curr_start
            end = curr_end
    
    res.append([start,end])
    print(f"Final result is :{res} ")

start_new("Merge Sorted Overlapping Intervals - 2 !!")
A = [[1, 3], [2, 6], [8, 10], [15, 18] ]
A = [ [2, 10], [4, 9], [6, 7] ]
merge_sroted_intervals(A)


def generateMatrix(A):
    r,c = 0,0 
    val = 1
    mat = [[0 for _ in range(A)]for _ in range(A)]
    print(mat)

    while(A > 1):
        for i in range(1,A):
            mat[r][c] = val 
            val += 1
            c += 1
        
        for i in range(1,A):
            mat[r][c] = val 
            val += 1
            r += 1
        
        for i in range(1,A):
            mat[r][c] = val 
            val += 1
            c -= 1
        
        for i in range(1,A):
            mat[r][c] = val 
            val += 1
            r -= 1
        
        r += 1
        c += 1
        A -= 2
    
    if A ==1 :
        mat[r][c] = val
       
    print(mat)


start_new("Spiral Order Matrix II !!")
A = 5
generateMatrix(A)


def find_in_2D_array_top_right(A,B):
    r = 0
    c = len(A[0]) - 1
    print(r,c)

    while r < len(A) and c >= 0:
        if A[r][c] == B:
            print(f"Elelemnt found at loc :{r,c}")
            print(f"Return value : {(r+1)*1009+(c+1)}") 
            return
        elif A[r][c] < B :
            r += 1
        else :
            c -= 1
    return -1

def find_in_2D_array_bottom_left(A,B):
    r = len(A) - 1
    c = 0
    print(r,c)

    while r >= 0  and c < len(A[0]) :
        if A[r][c] == B:
            print(f"Elelemnt found at loc :{r,c}")
            print(f"Return value : {(r+1)*1009+(c+1)}") 
            return
        elif A[r][c] < B :
            c += 1
        else :
            r -= 1
    return -1

start_new("Search in a row wise and column wise sorted matrix !!")
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2

A = [[2,8,8,8],[2,8,8,8],[2,8,8,8]]
B = 8

find_in_2D_array_top_right(A,B)
print('\n\n')
find_in_2D_array_bottom_left(A,B)

