import re

data = [i.strip() for i in open("data/day4.csv").readlines()]

# Part 1
score = 0
for row in data:
    cards = row.split(': ')[1]
    winners, entries = cards.split(' | ')
    winning_numbers = re.findall('\d+', winners)
    entry_numbers = re.findall('\d+', entries)

    wins = []
    for number in entry_numbers:
        if number in winning_numbers:
            wins.append(number)

    n = len(wins)
    if n > 0:
        score += (2 **(n-1))

print("Part 1 Answer: " + str(score))


# Part 2
games = dict()
for row in data:
    game_info = row.split(': ')[0]
    number = int(re.findall('\d+', game_info)[0])
    games[number] = 1

for row in data:
    row_number = data.index(row) + 1
    cards = row.split(': ')[1]
    winners, entries = cards.split(' | ')
    winning_numbers = re.findall('\d+', winners)
    entry_numbers = re.findall('\d+', entries)

    wins = []
    for number in entry_numbers:
        if number in winning_numbers:
            wins.append(number)

    n_per_card = len(wins)
    n_per_row = len(wins) * games[row_number]

    for i in range(1,n_per_card+1):
        games[row_number + i] += games[row_number]

print("Part 2 Answer: " + str(sum(games.values())))
