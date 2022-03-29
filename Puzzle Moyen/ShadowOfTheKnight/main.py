import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

# game loop
in_bomb_x = [0, w - 1]
in_bomb_y = [0, h - 1]
while True:
    bomb_dir = input()
    print(
        f"in_bomb_x : {in_bomb_x} x0 = {x0}   in_bomb_y : {in_bomb_y}  y0 = {y0}",
        file=sys.stderr,
        flush=True,
    )
    if "U" in bomb_dir:
        in_bomb_y[1] = y0
    elif "D" in bomb_dir:
        in_bomb_y[0] = y0 + 1
    else:
        in_bomb_y[0] = y0
        in_bomb_y[1] = y0
    if "L" in bomb_dir:
        in_bomb_x[1] = x0
    elif "R" in bomb_dir:
        in_bomb_x[0] = x0 + 1
    else:
        in_bomb_x[0] = x0
        in_bomb_x[1] = x0

    if in_bomb_x[0] == in_bomb_x[1]:
        x0 = in_bomb_x[0]
    else:
        x0 = (in_bomb_x[1] + in_bomb_x[0]) // 2
    if in_bomb_y[0] == in_bomb_y[1]:
        y0 = in_bomb_y[0]
    else:
        y0 = (in_bomb_y[1] + in_bomb_y[0]) // 2

    print(f"{x0} {y0}")
