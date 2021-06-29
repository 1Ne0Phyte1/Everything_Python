def fibo(n):
    x = 0
    y = 1
    r = 0
    while r<n:
        x,y = y,x+y
        r +=1
        print(x)
fibo(5)
