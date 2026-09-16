import csv

obj = [
    {"number": "1", "name": "siva"},
    {"number": "2", "name": "harshitha"},
    {"number": "3", "name": "amma"},
    {"number": "4", "name": "Nanna"},
    {"number": "5", "name": "thrinadh"},
]
csvfields = ["number", "name"]
fielname = "siva.csv"
with open(fielname, "w") as fp:
    dictwriter = csv.DictWriter(fp, fieldnames=csvfields)
    dictwriter.writeheader()
    dictwriter.writerows(obj)
    print("\n Dict write code success")
