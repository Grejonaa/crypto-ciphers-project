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
