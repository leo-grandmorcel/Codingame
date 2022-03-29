import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
neurons = []
grille = []
for i in range(height):
    line = input()  # width characters, each either 0 or .$
    grille.append(list(line))

for y in range(height):
    for x in range(width):
        if grille[y][x] == "0":
            x2 = y2 = x3 = y3 = -1
            for tx in range(x + 1, width):
                if grille[y][tx] == "0":
                    x2, y2 = tx, y
                    break
            for ty in range(y + 1, height):
                if grille[ty][x] == "0":
                    x3, y3 = x, ty
                    break
            print(f"{x} {y} {x2} {y2} {x3} {y3}")
