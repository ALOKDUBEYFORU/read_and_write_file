import csv

file1 = open(r'c:\temp\poem.txt')
dict1 = dict()
for readline in file1.readlines():
    for i in list(readline.split(' ')):
        i = i.replace('\n','')
        if i in dict1.keys():
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

print(dict1)

list1 = []

for i,j in dict1.items():
    if j == max(dict1.values()):
        list1.append(i)

print(list1)