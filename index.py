def fun2(n):
    sum = 0 
    it = 0 
    for i in range(1,n+1):
        sum+=i
        it = it + 1

    return sum,it

print(fun2(4))