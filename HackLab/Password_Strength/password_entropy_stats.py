#!/usr/bin/python3
import argparse
import math
import re
import prettytable

parser = argparse.ArgumentParser()
parser.add_argument("Password", help="Enter Password")
args = parser.parse_args()

password = args.Password

re_digit = '((?=.*\d).{0,100})'
re_lower = '((?=.*[a-z]).{0,100})'
re_Upper = '((?=.*[A-Z]).{0,100})'
re_special_char = '((?=.*[!@#$%^&*]).{0,100})'

count = 0
if bool(re.match(re_digit, password)) == True:
    count += 10
if bool(re.match(re_Upper, password)) == True:
    count += 26
if bool(re.match(re_lower, password)) == True:
    count += 26
if bool(re.match(re_special_char, password)) == True:
    count += 32

num_symbols = count
length = len(password)
entropy = math.log2(num_symbols ** length)
# print(count)


if entropy < 28:
    strength = ("Very Weak")
elif entropy < 36 and entropy > 28:
    strength = ("Weak")
elif entropy < 60 and entropy > 36:
    strength = ("Reasonable")
elif entropy < 127 and entropy > 60:
    strength = ('Strong')
elif entropy > 127:
    strength = ('Very Strong')

table = prettytable.PrettyTable(['Password', "Length", "Pool of unique characters", "Entropy", "Strength"])
table.add_row([password, length, num_symbols, entropy, strength])

print(table)
