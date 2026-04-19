def autokey_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    if not key:
        raise ValueError("Key nuk mund të jetë bosh!")

    cipher = ""
    key_stream = list(key)

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key_stream.pop(0)) - ord('A')

            c = (p + k) % 26
            cipher += chr(c + ord('A'))

            key_stream.append(char)
        else:
            cipher += char

    return cipher

def autokey_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    if not key:
        raise ValueError("Key nuk mund të jetë bosh!")
         
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
