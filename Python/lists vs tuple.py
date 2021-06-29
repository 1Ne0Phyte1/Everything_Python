def example():
    return 15,19

a,b = example()
x = [64,5,4,4,15,19]

print (a)
print (b)
print (x)
print (x[3])

x.append(12)
print(x)

x.insert(2,78)# 2 here represents id, not a number
print(x)

x. remove(78)
print(x)
print(x.index(15))
print(x.count(4))
x.sort()
print(x)
x.reverse()
print(x)
