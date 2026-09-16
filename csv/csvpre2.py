import csv

obj = [
    {"number": "1", "name": "siva", "branch": "ece"},
    {"number": "2", "name": "harshitha", "branch": "cse"},
    {"number": "3", "name": "amma", "branch": "home"},
    {"number": "4", "name": "Nanna", "branch": "eee"},
    {"number": "5", "name": "thrinadh", "branch": "ece"},
]
csvfields = ["number", "name", "branch"]
filename = "siva2.csv"
with open(filename, "w") as fp:
    dictwrite = csv.DictWriter(fp, fieldnames=csvfields)
    dictwrite.writeheader()
    dictwrite.writerows(obj)
    print("\n print end")
