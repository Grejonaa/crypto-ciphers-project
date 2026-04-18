def get_rail_lengths(text_length, rail_count):
    lengths = [0] * rail_count
    current_row = 0
    direction = 1

    for _ in range(text_length):
        lengths[current_row] += 1

        if current_row == 0:
            direction = 1
        elif current_row == rail_count - 1:
            direction = -1

        current_row += direction

    return lengths


def redefence_decrypt(ciphertext, key):
    rail_count = len(key)

    
    order = get_key_order(key)

    
    lengths = get_rail_lengths(len(ciphertext), rail_count)

    
    rails = [""] * rail_count
    index = 0

    for i in order:
        length = lengths[i]
        rails[i] = ciphertext[index:index + length]
        index += length

    
    result = []
    pointers = [0] * rail_count

    current_row = 0
    direction = 1

    for _ in range(len(ciphertext)):
        result.append(rails[current_row][pointers[current_row]])
        pointers[current_row] += 1

        if current_row == 0:
            direction = 1
        elif current_row == rail_count - 1:
            direction = -1

        current_row += direction

    return "".join(result)