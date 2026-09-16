import csv

try:
    with open("siva.csv", "r") as fp:
        dictredcsv = csv.DictReader(fp)
        for rec in dictredcsv:
            for key, val in rec.items():
                print("\t {}--->{}".format(key, val))
            print()
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("value will  give perfet")
