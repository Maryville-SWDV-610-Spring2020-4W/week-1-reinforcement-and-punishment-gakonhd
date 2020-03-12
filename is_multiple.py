def is_multiple(n, m):
    #check if n = mi
    #then we can check if n/m = i is integer or not
    division = n/m
    if division.is_integer():
        return True # n is a multiple of m 
    else:
        return False # n is not

print(is_multiple(10,2)) #true
print(is_multiple(10,5)) #true
print(is_multiple(10,4)) #false - 2.5
print(is_multiple(10,3)) # false 3.33333
print(is_multiple(10,10)) #1
