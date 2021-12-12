a = [5,7,6,8,9,2,4,3,1,6,8]

x= int(input("Enter a number: "))

for n in range (len(a)):
    a.sort()
    if a[n] == x:
        print(f'{n}')
