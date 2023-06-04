import csv
data=[]

with open("archive_dataset.csv", 'r')as f:
    info = csv.reader(f)
    for i in info:
        data.append(i)

headers = data[0]
star_data = data[1:]

#convert the names into lower case
for i in star_data:
  i[2] = i[2].lower()

#sorting the star names in alphabetic order
star_data.sort(key=lambda star_data:star_data[2] )

# with open("archive_dataset_sorted.csv", 'a+')as f:
#     info = csv.writer(f)
#     info.writerow(headers)
#     info.writerows(planet_data)

#remove blanks lines in the csv
with open("archive_dataset_sorted.csv",'r')as f, open('archive_dataset_sorted1.csv', 'w',newline='') as output:
    info = csv.writer(output)
    for i in csv.reader(f):
        if any(j.strip() for j in i):
               info.writerow(i)
