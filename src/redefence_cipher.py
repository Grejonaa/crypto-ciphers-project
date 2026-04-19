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

def build_zigzag_rails(plaintext, rail_count):
    if rail_count <= 0:
        raise ValueError("Numri i rails duhet te jete me i madh se 0.")

    if rail_count == 1:
        return [plaintext]

    if len(plaintext) <= 1:
        rails = [""] * rail_count
        if len(plaintext) == 1:
            rails[0] = plaintext
        return rails

    rails = [""] * rail_count
    current_row = 0
    direction = 1  # 1 = poshte, -1 = lart

    for ch in plaintext:
        rails[current_row] += ch

        if current_row == 0:
            direction = 1
        elif current_row == rail_count - 1:
            direction = -1

        current_row += direction

    return rails


def get_key_order(key):
    indexed_key = list(enumerate(key))
    sorted_key = sorted(indexed_key, key=lambda item: (item[1].lower(), item[0]))
    order = [index for index, _ in sorted_key]
    return order


def redefence_encrypt(plaintext, key):
    if not isinstance(plaintext, str) or not isinstance(key, str):
        raise TypeError("Plaintext dhe key duhet te jene string.")

    if len(key) == 0:
        raise ValueError("Key nuk mund te jete bosh.")

    rail_count = len(key)
    rails = build_zigzag_rails(plaintext, rail_count)
    order = get_key_order(key)
    ciphertext = "".join(rails[i] for i in order)

    return ciphertext, rails, order
