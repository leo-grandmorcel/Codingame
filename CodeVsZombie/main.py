import sys
import math


class Humain:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return f"ID = {self.id}  Position = {self.x},{self.y}"


class Zombie:
    def __init__(self, id, x, y, xnext, ynext):
        self.id = id
        self.x = x
        self.y = y
        self.xnext = xnext
        self.ynext = ynext

    def __str__(self):
        return f"ID={self.id} Position = {self.x},{self.y} {self.xnext},{self.ynext}"


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


while True:
    humains = []
    zombies = []
    direction_x = 8000
    direction_y = 4500
    x, y = [int(i) for i in input().split()]

    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humains.append(Humain(human_id, human_x, human_y))

    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [
            int(j) for j in input().split()
        ]
        zombies.append(
            Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)
        )

    closest_humain_dist = 100000
    for humain in humains:
        closest_zombie_dist = 1000000
        closest_zombie = Zombie(0, 0, 0, 0, 0)
        for zombie in zombies:
            zombie_dist_humain = distance(humain.x, humain.y, zombie.x, zombie.y)
            if zombie_dist_humain < closest_zombie_dist:
                closest_zombie = zombie
                closest_zombie_dist = zombie_dist_humain
        zombie_dist_player = distance(x, y, closest_zombie.x, closest_zombie.y)
        if math.ceil(closest_zombie_dist / 400) >= math.ceil(
            (zombie_dist_player - 2000) / 1000
        ):
            humain_distance = distance(x, y, humain.x, humain.y)
            if humain_distance < closest_humain_dist:
                direction_x = closest_zombie.xnext
                direction_y = closest_zombie.ynext

    NoDanger = True
    for zombie in zombies:
        for humain in humains:
            if distance(humain.x, humain.y, zombie.x, zombie.y) < distance(
                x, y, zombie.x, zombie.y
            ):
                NoDanger = False
                break
        if not NoDanger:
            break

    if NoDanger:
        direction_x = int(sum([zombie.x for zombie in zombies]) / len(zombies))
        direction_y = int(sum([zombie.y for zombie in zombies]) / len(zombies))
    print(f"{direction_x} {direction_y}")
