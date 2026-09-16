import csv

boj = ("4", "ravi", "match")
filename = "siva3.csv"
with open(filename, "a") as fp:
    cw = csv.writer(fp)
    cw.writerow(boj)
    print("\n program completeed")
