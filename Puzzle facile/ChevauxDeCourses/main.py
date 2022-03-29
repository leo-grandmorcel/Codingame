nb_horses = int(input())
powers = sorted([int(input()) for _ in range(nb_horses)])
min_puissance = 10000000
result = 0
for index in range(nb_horses - 1):
    power1 = powers[index]
    power2 = powers[index + 1]
    if abs(power1 - power2) < min_puissance:
        min_puissance = abs(power1 - power2)
print(min_puissance)
