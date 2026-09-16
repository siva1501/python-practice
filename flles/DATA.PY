import csv


WINNER_COLUMN = "winner"


def calculate():
    winner_count = {}

    with open("matches.csv", encoding="utf-8") as matches_file:
        matches_reader = csv.DictReader(matches_file)

        for match in matches_reader:
            winning_team = match[WINNER_COLUMN]

            if winning_team:
                if winning_team in winner_count:
                    winner_count[winning_team] += 1
                else:
                    winner_count[winning_team] = 1

    return winner_count


def plot(winner_count):
    for team, wins in winner_count.items():
        print(f"{team}: {wins}")


def execute():
    winner_count = calculate()
    plot(winner_count)


execute()