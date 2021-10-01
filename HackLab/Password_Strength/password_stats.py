import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Password", help="Enter Password")
args = parser.parse_args()

v=args.Password
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
else:
    print("You have entered an invalid password.")