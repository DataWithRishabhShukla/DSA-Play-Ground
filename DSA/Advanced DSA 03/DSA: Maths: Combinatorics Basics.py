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