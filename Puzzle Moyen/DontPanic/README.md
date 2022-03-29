Vous devez aider les clones à atteindre la sortie pour s'échapper de la zone du générateur.

La zone est rectangulaire et de taille variable. Elle est composée de plusieurs étages (0 = étage inférieur) et chaque étage comporte plusieurs positions possible pour les clones (0 = position la plus à gauche, width - 1 = position la plus à droite).

L'objectif est de sauver au moins un clone en un nombre limité de tours.

En détail :
    Les clones sortent d'un unique générateur à intervalles réguliers, tous les 3 tours. Le générateur est placé à l'étage 0. Les clones sortent en se dirigeant vers la droite.

    Les clones avancent d'une position par tour en ligne droite, dans leur direction actuelle.

    Un clone est détruit par un laser s'il dépasse la position 0 ou la position width - 1.

    La zone dispose d'ascenseurs pour monter d'un étage à l'autre. Quand un clone arrive sur une position où se trouve un ascenseur, il monte d'un étage. Monter d'un étage prend un tour de jeu. Au tour suivant le clone continue sa progression dans la direction qu'il avait avant de monter.

    À chaque tour vous pouvez soit ne rien faire, soit bloquer le clone de tête (c-à-d celui qui est sorti le plus tôt).

    Une fois qu'un clone est bloqué, vous ne pouvez plus agir dessus. Le clone suivant prend le rôle de clone de tête et peut être bloqué à son tour.

    Quand un clone avance ou se trouve sur une position sur laquelle se situe un clone bloqué, il change de direction.

    Si un clone bloque au pied d'un ascenseur, l'ascenseur ne peut plus être utilisé.

