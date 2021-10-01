#!/usr/bin/python3
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("num_symbols", help="character set or number of symbols", type=int)
parser.add_argument("length", help="password length in characters", type=int)
args = parser.parse_args()

# E = log2(R^L)
# R = pool size
# L = Password Length

# Pool              Elements            Pool size

# Digits            0-9	                10

# Lower case        a-z                 26
# Latin letters

# Upper case        A-z                 26
# Latin letters

# Latin letters     a-z, A-Z 	        52

# Alphanumeric 	    a-z, 0-9	        36

# Alphanumeric &    a-z, A-Z, 0-9       62
# Upper Case

# Special symbols   ~!@#$%^&*()-=_      32
# (typical U.S.     +[{]}\|;':",.<>/?
# keyboard)

print (math.log2(args.num_symbols**args.length))