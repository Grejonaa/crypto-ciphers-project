def autokey_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    full_key = key + plaintext
    cipher = ""

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(full_key[i]) - ord('A')

        c = (p + k) % 26
        cipher += chr(c + ord('A'))

    return cipher


def autokey_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ""

    for i in range(len(ciphertext)):
        k = ord(key[i]) - ord('A')
        c = ord(ciphertext[i]) - ord('A')

        p = (c - k) % 26
        letter = chr(p + ord('A'))

        plaintext += letter
        key += letter 

    return plaintext


# MAIN
choice = input("Zgjedh (E)ncrypt ose (D)ecrypt: ").lower()

if choice == 'e':
    plaintext = input("Shkruaj plaintext: ")
    key = input("Shkruaj key: ")
    print("Ciphertext:", autokey_encrypt(plaintext, key))

elif choice == 'd':
    ciphertext = input("Shkruaj ciphertext: ")
    key = input("Shkruaj key: ")
    print("Plaintext:", autokey_decrypt(ciphertext, key))

else:
    print("Zgjedhje jo valide!")
