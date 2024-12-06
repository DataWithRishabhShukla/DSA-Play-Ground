import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Combinatorics Basics")
print("Problem  - Priting the Pascal Triangle !!\n")


def pascal_triangle(n):
    ans = [[0 for i in range(n)] for j in range(n)]
    
    ans[0][0] = 1

    for i in range(1,n):
        for j in range(0, i+1):
            if j == 0 or j == i :
                ans[i][j] = 1
            
            else :
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]

    print(ans)



pascal_triangle(3)


import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Combinatorics Basics")
print("Problem  - Excel Column Title !!\n")

def get_excel_col(A):
    hm = dict()
    ans = ''

    for i in range(1,27):
        hm[i] = chr(i-1+65)

    print(hm)

    while A != 0:
        rem = A % 26
        A = A // 26

        if rem == 0:
            rem = 26
            N = N-1

        ans = hm[rem] + ans
    
    print(ans)

get_excel_col(30)
    


import os 

os.system("clear")

print("Section  - Advance DSA 03")
print("Module   - DSA: Maths: Combinatorics Basics")
print("Problem  - Calculate the nCr !!\n")


def get_ncr(N):
    pass

def calculateRangeProduct(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
