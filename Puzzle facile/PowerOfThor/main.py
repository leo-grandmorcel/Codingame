light_x, light_y, initial_thor_x, initial_thor_y = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())  # Do not remove this line.
    move = ""
    if initial_thor_y > light_y:
        move += "N"
        initial_thor_y -= 1
    elif initial_thor_y < light_y:
        move += "S"
        initial_thor_y += 1
    if initial_thor_x > light_x:
        move += "W"
        initial_thor_x -= 1
    elif initial_thor_x < light_x:
        move += "E"
        initial_thor_x += 1
    print(move)
