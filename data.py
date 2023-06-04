import csv 

dataset_1 = []
dataset_2 = []
with open("dwarf_stars.csv",'r')as f:
    c=csv.reader(f)
    for i in c:
        dataset_1.append(i)

with open("archive_dataset_sorted1.csv",'r') as a:
    d=csv.reader(a)
    for g in d:
        dataset_2.append(g)

header1 = dataset_1[0]
header2 = dataset_2[0]
header = header1 + header2

starData1 = dataset_1[1:]
starData2 = dataset_2[1:]
star_data = []

for index,value in enumerate(starData1):
    star_data.append(starData1[index] + starData2[index])

with open("merged_data.csv",'a+') as b:
    s=csv.writer(b)
    s.writerow(header)
    s.writerows(star_data)
    