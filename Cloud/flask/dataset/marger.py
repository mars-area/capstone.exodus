import csv
reader = csv.reader(open('dataset/data-apple.csv'))
reader1 = csv.reader(open('dataset/data-banana.csv'))
reader2 = csv.reader(open('dataset/data-mango.csv'))
reader3 = csv.reader(open('dataset/data-tomatoes.csv'))
f = open('dataset/datafruit.csv', 'w', newline='')
writer = csv.writer(f)
for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
for row in reader2:
    writer.writerow(row)
for row in reader3:
    writer.writerow(row)
f.close()