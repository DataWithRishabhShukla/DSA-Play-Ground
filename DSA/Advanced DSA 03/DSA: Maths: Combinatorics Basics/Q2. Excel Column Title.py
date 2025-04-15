
def convertToTitle(A):
    d = {i:chr(i+64) for i in range(1,27)}
    print(d)
    ans = ''
    while A > 0 :
        rem = A % 26 
        A = A // 26 
        if rem == 0:
            ans += 'Z'
            A -= 1
        else :
            ans += d[rem]
    #ans =  ans[::-1]   
    print(ans)

convertToTitle(27)        
        



