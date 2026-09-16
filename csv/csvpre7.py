import csv

obj = [["5", "ammu", "home"], ["6", "ram", "cse"]]
with open("siva3.csv", "a") as fp:
    cw = csv.writer(fp)
    cw.writerows(obj)
    print("\n program will completed")
