def autokey_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    if not key:
        raise ValueError("Key nuk mund të jetë bosh!")

    cipher = ""
    full_key = key

    for ch in plaintext:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            k = ord(full_key[0]) - ord('A')
            full_key = full_key[1:] + ch

            c = (p + k) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch

    return cipher

def autokey_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    full_key = key
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(full_key[key_index]) - ord('A')

            p = (c - k) % 26
            letter = chr(p + ord('A'))

            plaintext += letter
            full_key += letter
            key_index += 1
        else:
            # ruan spaces, numra, simbole pa i ndryshu
            plaintext += char

    return plaintext