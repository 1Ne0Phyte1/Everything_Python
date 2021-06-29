#input from user
'''
name = input('What is your name?: ')
print('Hello',name)
'''

import statistics
exList = [2,3,5,7,4,6,7,4,2,5,3,2,7]
x = statistics.mean(exList)
print(x)
x = statistics.median(exList)
print(x)
x = statistics.mode(exList)
print(x)
x = statistics.stdev(exList)
print(x)
x = statistics.variance(exList)
print(x)
