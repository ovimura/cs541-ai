square = [[0]*5 for x in range(5)]

scratch = [[0]*5 for x in range(5)]


def flood(s, color, x, y):
    global scratch
    if (not (x >= 0 and x <= 4 and y >= 0 and y <= 4)):
        return
    if (scratch[x][y]):
        return
    if (square[x][y] != color):
        return
    scratch[x][y] = True
    flood(scratch, color, x - 1, y)
    flood(scratch, color, x + 1, y)
    flood(scratch, color, x, y - 1)
    flood(scratch, color, x, y + 1)

print(square)
flood(scratch, 0, 4,0)
print(scratch)

