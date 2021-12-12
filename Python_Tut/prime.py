def prime(x):
    return all(x%i!=0 for i in range(2,x//2))


if(prime(13)):
    print("is prime")
