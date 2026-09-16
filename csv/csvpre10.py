import csv

try:
    with open("umpires.csv", "r") as fp:
        csr = csv.DictReader(fp)
        for rec in csr:
            for val in rec.items():
                print("\t{}".format(val), end="")
            print()
except FileNotFoundError:
    print("\t file not founf please try agin")
