
def solve(A):
    r = A + 1
    c = A + 1

    ans = [[-1 for _ in range(c)] for _ in range(c)]
    i,j = 0,0

    for i in range(r):
        for j in range(c):
            if j > i :
                continue
            
            if j == 0 or i == j :
                ans[i][j] = 1
            else :
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
    
    for row in ans :
        print(row)

solve(4)