# CSV ALL WORKS
import csv

obj = [
    {"name": "siva", "branch": "ECE", "CGPA": "7.8"},
    {"name": "haishi", "branch": "EEE", "CGPA": "8.8"},
    {"name": "ram", "branch": "CSE", "CGPA": "9.9"},
    {"name": "thrinadh", "branch": "Match", "CGPA": "7.4"},
    {"name": "naveen", "branch": "CIVIL", "CGPA": "8.5"},
    {"name": "Aravindh", "branch": "ECE", "CGPA": "10.0"},
]
csvfields = ["name", "branch", "CGPA"]
filename = "siva4.csv"
with open(filename, "w") as fp:
    dictwrite = csv.DictWriter(fp, fieldnames=csvfields)
    dictwrite.writeheader()
    dictwrite.writerows(obj)
    print("\n program completed")

obj = ["kishore", "EEE", "5.5"]
with open("siva4.csv", "a") as fp:
    dictwrite = csv.writer(fp)
    dictwrite.writerow(obj)

with open("siva4.csv", "r") as fp:
    dcsw = csv.DictReader(fp)
    for rec in dcsw:
        for key, val in rec.items():
            print("\t {}------->{}".format(key, val))
        print()

with open("siva4.csv", "r") as fp:
    dcsw = csv.DictReader(fp)
    for rec in dcsw:
        print("\t {}".format(rec["name"]))

with open("siva4.csv", "r") as fp:
    csw = csv.DictReader(fp)
    for rec in csw:
        print("\t {}-------->{}".format(rec["branch"], rec["CGPA"]))
