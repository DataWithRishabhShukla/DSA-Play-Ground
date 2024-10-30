def start_new(func_name):
    import os 
    os.system("clear")
    print(f"Proessing for : {func_name}!!!\n")


from functools import cmp_to_key

def cmp_custom(x,y):
    if x + y > y + x:
        return -1
    elif x == y :
        return 0
    else :
        return 1
    
start_new("Q1. Largest Number")

arr = [3, 30, 34, 5, 9]
nums = [str(num) for num in arr]
print(nums)

nums.sort(key= cmp_to_key(cmp_custom))

print(nums)
print(f"\n String representaion is : {''.join(nums)}")


def count_factors(x):
    count = 0
    i = 1
    while i*i <= x:
        if x %i == 0:
            if x /i == i: 
                count += 1
            else :
                count += 2
        i += 1
    
    #print(f"number of count for {x} are {count} !!")
    return count

def cmp_custom_facotrs(x,y):
    if count_factors(x) == count_factors(y):
        if x < y :
            return -1 
        elif x == y :
            return 0
        else :
            return 1
    elif count_factors(x) < count_factors(y):
        return -1
    else :
        return 1

start_new("Q3. Factors sort !!")
count_factors(9)

A = [6, 8, 9]
print(f"Array before sorting : {A}")
A.sort(key = cmp_to_key(cmp_custom_facotrs))
print(f"Array after sorting : {A}")



start_new("Q5. Partition Index !!")