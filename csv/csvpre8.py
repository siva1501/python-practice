import csv

try:
    with open("siva3.csv", "r") as fp:
        cws = csv.reader(fp)
        for val in cws:
            for rec in val:
                print("\t {}".format(rec), end="")
            print()
except FileExistsError:
    print("\t file not exits")
