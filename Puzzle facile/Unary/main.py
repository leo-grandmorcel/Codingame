message = input()


def char2bin(texte):
    result = bin(ord(texte))[2:]
    result = "0" * (7 - len(result)) + result
    return result


def text2bin(texte):
    return "".join(char2bin(char) for char in texte)


def bin2unaire(binary):
    result = ""
    previous_bit = None
    for bit in binary:
        if bit == previous_bit:
            result += "0"
        else:
            if bit == "1":
                result += " 0 0"
            else:
                result += " 00 0"
        previous_bit = bit
    return result[1:]


print(bin2unaire(text2bin(message)))
