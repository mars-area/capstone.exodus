#!/usr/bin/python
import csv
import os
import re

data = []
text1 = 'TRAIN'
text2 = 'tomatoes'
i = 0

openFile = open('dataset/datafruit.csv', 'r', newline='')
for row in openFile:
    string = []
    rawRow = row.strip()
    string.append(text1)
    string.append(rawRow)
    string.append(text2)
    string = ','.join(string)
    data.append(string)
    i += 1
    if i > 999:
        break
openFile.close()

print('string = ', string)
print('data = ', data)

with open('dataset/check.csv', mode='w+', newline='') as dataTrain:
    writer = csv.writer(dataTrain)
    for item in data:
        print(item)
        writer.writerow([item])