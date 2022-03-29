(
    nb_floors,
    width,
    nb_rounds,
    exit_floor,
    exit_pos,
    nb_total_clones,
    nb_additional_elevators,
    nb_elevators,
) = [int(i) for i in input().split()]
ascenceur = {}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    ascenceur[elevator_floor] = elevator_pos


def reponse(direction, chaine):
    if direction == chaine:
        print("BLOCK")
    else:
        print("WAIT")


while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]
    if clone_floor != -1 and clone_pos != -1 and direction != None:
        if clone_floor == exit_floor:
            if clone_pos - exit_pos >= 0:
                reponse(direction, "RIGHT")
            else:
                reponse(direction, "LEFT")
        else:
            if clone_pos - ascenceur[clone_floor] == 0:
                print("WAIT")
            elif clone_pos - ascenceur[clone_floor] > 0:
                reponse(direction, "RIGHT")
            else:
                reponse(direction, "LEFT")
    else:
        print("WAIT")
