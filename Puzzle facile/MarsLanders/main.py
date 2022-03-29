import sys
import math

surface_n = int(input())
mapping = []
coordonne_landing = []
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    mapping.append([land_x, land_y])

print(mapping, file=sys.stderr, flush=True)
mapping.sort()
last_point = 0
last_alt = 0
for x in range(len(mapping)):
    if mapping[x][0] + 1000 >= last_point and mapping[x][1] == last_alt:
        coordonne_landing.append((mapping[x][0] + last_point) // 2)
        coordonne_landing.append(mapping[x][1])
        break
    else:
        last_point = mapping[x][0]
        last_alt = mapping[x][1]

print(coordonne_landing, file=sys.stderr, flush=True)
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if abs(v_speed) > 40 and power < 4:
        power += 1
    elif abs(v_speed) < 0 and power > 0:
        power -= 1

    print(f"{rotate} {power}")
