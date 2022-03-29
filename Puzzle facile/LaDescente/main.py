while True:
    hauteur_montagne = [int(input()) for _ in range(8)]
    iteration = 0
    montagne_to_destruct = 0
    index_montagne = 0
    while iteration < 8:
        if montagne_to_destruct < hauteur_montagne[iteration]:
            montagne_to_destruct = hauteur_montagne[iteration]
            index_montagne = iteration
        iteration += 1
    print(index_montagne)
