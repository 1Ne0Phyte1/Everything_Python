gradeDict = {'Kelly':89,'David':65,'Samantha':99}
print(gradeDict)
print(gradeDict['David'])
gradeDict['David']=88
print(gradeDict)
gradeDict['Joy']= 45
print(gradeDict)
del gradeDict['David']
print(gradeDict)

gradeDict = {'Kelly':[89,45,78,55],
             'Joy':[45,67,5,3],
             'Samantha':[99,32,25,36]}
print (gradeDict)
print (gradeDict['Joy'])
print (gradeDict['Joy'][2])
