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

# Empty list of games, and initialized # for power_sum
games = []
power_sum = 0

# Pretty minimal change here versus part 1 to get the answer! Nice.
for entry in data:
    games.append(entry.split(': ')[1])

for game in games:
    red = re.findall('\d+ red', game)
    green = re.findall('\d+ green', game)
    blue = re.findall('\d+ blue', game)

    power = find_max_color(red) * find_max_color(blue) * find_max_color(green)
    power_sum += power

print(power_sum)
