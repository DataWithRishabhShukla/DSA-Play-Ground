import os
def clear():
    os.system('clear')
    

from random import randint
a = [randint(10,100) for i in range(20)]
print(a)


b = [(x,x**2,x**3) for x in range(10)]
print(b)


s = ['10','20','30','40']
a = [int(_) for _ in s ]
print(a)



nums = [num for num in range(10,31) if num % 2 == 0]
print(nums)

clear() 
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,15]
