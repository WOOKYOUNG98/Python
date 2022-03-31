import csv

file = open("./myvenv/09_파일 입출력/student.csv", "r", newline="", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close