#a = [5,7,6,8,9,2,4,3,1,6,8]
a = []
for i in range(101):
    a.append(i)
x= int(input("Enter a number: "))

for n in range (len(a)):
    a.sort()
    if a[n] == x:
        print(f'{n}')
    else:
        pass
print("Number is out of rannge")
