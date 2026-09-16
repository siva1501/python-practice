import csv

headnames = ["number", "name", "branch"]
obj = [["1", "siva", "ece"], ["2", "naveen", "ece"], ["3", "thinadh", "eee"]]
with open("siva3.csv", "w") as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(headnames)
    csvwriter.writerows(obj)
    print("\n hii program ended")
