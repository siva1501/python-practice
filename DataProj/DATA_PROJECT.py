import csv
def calculate():
    batting_team_count = {}
    with open("matches.csv", "r") as file:
        matches_reader = csv.DictReader(file)
        for match in matches_reader:
            batting_team = match["batting_team"]
            if batting_team in batting_team_count:
                batting_team_count[batting_team] += 1
            else:
                batting_team_count[batting_team] = 1
    return batting_team_count
def plot(result):
    print(result)
def execute():
    result = calculate()
    plot(result)
execute()