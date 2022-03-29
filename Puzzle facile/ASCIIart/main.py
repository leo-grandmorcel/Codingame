class Letter:
    width = 0
    height = 0

    def __init__(self):
        self.skin = []


Letter.width = int(input())
Letter.height = int(input())
text = input()

letters = [Letter() for _ in range(27)]

for _ in range(Letter.height):
    row = input()
    for letter_index in range(27):
        partial_skin = row[
            letter_index * Letter.width : (letter_index + 1) * Letter.width
        ]
        letters[letter_index].skin.append(partial_skin)

for line_number in range(Letter.height):
    for char in text:
        char = char.upper()
        if "A" <= char <= "Z":
            letter_index = ord(char) - ord("A")
        else:
            letter_index = 26
        letter = letters[letter_index]
        print(letter.skin[line_number], end="")
    print()
