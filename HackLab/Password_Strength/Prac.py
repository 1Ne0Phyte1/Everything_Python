import math
import re
import prettytable

Passwords = ["placements","PLACEMENTS","7845985484","PlAcEmEnTs","P1Ac3m3nTs","P!Ac3m3nT$"]
table = prettytable.PrettyTable(['Password',"Length","Pool of unique characters","Entropy","Strength"])
for i in range(len(Passwords)):

    re_digit = '((?=.*\d).{0,100})'
    re_lower = '((?=.*[a-z]).{0,100})'
    re_Upper = '((?=.*[A-Z]).{0,100})'
    re_special_char = '((?=.*[!@#$%^&*]).{0,100})'


    count = 0
    if bool(re.match(re_digit,Passwords[i])) ==True:
        count +=10
    if bool(re.match(re_Upper,Passwords[i])) == True:
        count += 26
    if bool(re.match(re_lower,Passwords[i])) == True:
        count += 26
    if bool(re.match(re_special_char,Passwords[i])) == True:
        count += 32


    num_symbols = count
    length = len(Passwords[i])
    entropy = math.log2(num_symbols**length)
    # print(count)


    if entropy < 28 :
        strength = ("Very Weak")
    elif entropy <36 and entropy>29:
        strength =("Weak")
    elif entropy<60 and entropy > 37:
        strength =("Reasonable")
    elif entropy< 127 and entropy > 61:
        strength =('Strong')
    elif entropy > 128:
        strength =('Very Strong')


    table.add_row([Passwords[i],length,num_symbols,entropy,strength])

print(table)
