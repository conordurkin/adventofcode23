data = [i.strip() for i in open("data/day3.csv").readlines()]

coords = dict()
for row in range(len(data)):
    for col in range(len(data[row])):
        coords[(row, col)] = data[col][row]

def is_symbol(box):
    if (box.isdigit()) or (box == '.'):
        return False
    else:
        return True

def check_adjacents(x, y):
    valid = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x+i, y+j) in coords:
                if is_symbol(coords[x+i, y+j]):
                    valid = True
                else:
                    pass
    return valid

total = 0

for row in range(len(data)):
    num = '0'
    valid_num = False

    for col in range(len(data[row])):

        box = data[row][col]

        if box.isdigit():
            num += str(box)

            if check_adjacents(col, row):
                valid_num = True

        else:
            if num != '0':
                num = int(num)
                if valid_num:
                    total += num
                num = '0'
                valid_num = False
            else:
                continue

    if num != '0':
        num = int(num)
        if valid_num:
            total += num
        num = '0'
        valid_num = False

print(total)
