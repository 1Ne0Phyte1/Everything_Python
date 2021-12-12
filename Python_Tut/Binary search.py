a = [4, 2, 5, 6, 4, 3, 3, 5, 5, 7, 5, 7, 7, 3, 8, 9, 5, 5, 10, 2]
x = int(input("Enter a number to find: "))
a.sort()
L = 0
U = len(a)
while L<= U:
    mid = (L+U)//2
    if x == a[mid]:
        print("Your value is at position: ",mid)
        break
    else:
        if x > a[mid]:
            L = mid
        else:
            U = mid
