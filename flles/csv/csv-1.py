import csv
mydict = [
    {"name": "Siva", "branch": "CSE", "year": 4, "cgpa": 8.7},
    {"name": "Ravi", "branch": "ECE", "year": 3, "cgpa": 7.9},
    {"name": "Anil", "branch": "CSE", "year": 2, "cgpa": 9.2},
    {"name": "Priya", "branch": "EEE", "year": 4, "cgpa": 8.4}
]
csvfile=["name","branch","year","cgpa"]
fieldnames="siva.csv"
with open(fieldnames,"w") as fp:
    dictwrite=csv.DictWriter(fp,fieldnames=csvfile)
    dictwrite.writeheader()
    dictwrite.writerows(mydict)
    print("\n ok")