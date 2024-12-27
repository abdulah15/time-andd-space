def fun3(n):
    sum = 0 
    it = 0 
    
    for i in range(1,n+1):
        for j in range(1,i+1):

            sum+=i
            it = it + 1

    return sum,it

print(fun3(4))