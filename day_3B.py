data = [i.strip() for i in open("data/day3.csv").readlines()]

coords = dict()
for row in range(len(data)):
    for col in range(len(data[row])):
        coords[(row, col)] = data[col][row]

def check_adjacents_for_gear(x, y):
    valid = False
    location = None
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x+i, y+j) in coords:
                if (coords[x+i, y+j]) == '*':
                    valid = True
                    location = (x+i, y+j)
                else:
                    pass
    return valid, location

total = 0
gear_locations = dict()

for row in range(len(data)):
    num = '0'
    gear_adjacent = False


    for col in range(len(data[row])):

        box = data[row][col]

        if box.isdigit():
            num += str(box)

            if check_adjacents_for_gear(col, row)[0]:
                gear_location = check_adjacents_for_gear(col, row)[1]
                gear_adjacent = True

        else:
            if num != '0':
                num = int(num)
                if gear_adjacent:
                    if gear_location in gear_locations:
                        gear_locations[gear_location].append(num)
                    else: gear_locations[gear_location] = [num]
                num = '0'
                gear_adjacent = False
            else:
                continue


    if num != '0':
        num = int(num)
        if gear_adjacent:
            if gear_location in gear_locations:
                gear_locations[gear_location].append(num)
            else: gear_locations[gear_location] = [num]
        num = '0'
        gear_adjacent = False

gear_product = 0
for gear in gear_locations:
    if len(gear_locations[gear]) == 2:
        gear_product += (gear_locations[gear][0] * gear_locations[gear][1])

print(gear_product)
