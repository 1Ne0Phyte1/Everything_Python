def BS(x, a):
    L = 0
    U = len(a)
    mid = (L+U)//2
    if x == a[mid]:
        print("Yes")
    elif x< a[mid]:
        U = mid
        print("U",U)
    elif x > a[mid]:
        L = mid
        print("L",L)
a = [1,2,3,4,5,6,7,8,9]
BS(5, a)

