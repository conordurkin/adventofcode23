import re

data = [i.strip() for i in open("data/day2.csv").readlines()]

# Set max for each color here
red_max = 12
green_max = 13
blue_max = 14

# Define function to take the max of a given color's pulls from a list of pulls
def find_max_color(color):
    n = 0
    for group in color:
        count = int(group.split(' ')[0])
        if count > n:
            n = count
    return n

# Empty list of games, and initialized # for valid total games
games = []
valid_total = 0

# Clean the data, keep only stuff after "Game X: " as the game-related data
for entry in data:
    games.append(entry.split(': ')[1])

# For each game, find set of each color's pulls
for game in games:
    red = re.findall('\d+ red', game)
    green = re.findall('\d+ green', game)
    blue = re.findall('\d+ blue', game)

    # confirm whether a max pull is valid or not. Only keep valid entries.
    if (find_max_color(red) <= red_max) & (find_max_color(blue) <= blue_max) & (find_max_color(green) <= green_max):
        valid_total += games.index(game)+1

print(valid_total)
