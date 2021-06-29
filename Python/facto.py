# 5! = 5*4*3*2*1



def fa(x):
    if x<2:
        return 1
    return x*fa(x-1)


   
print(fa(3))
