from autokey import autokey_encrypt, autokey_decrypt
from redefence_cipher import redefence_encrypt, redefence_decrypt

algorithm = input("Zgjedh algoritmin (A)utokey ose (R)edefence: ").lower()
choice = input("Zgjedh (E)ncrypt ose (D)ecrypt: ").lower()

if algorithm == 'a':
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

elif algorithm == 'r':
    if choice == 'e':
        plaintext = input("Shkruaj plaintext: ")
        key = input("Shkruaj key: ").replace(" ", "").strip()

        if key == "":
            print("Gabim: key nuk mund te jete bosh.")
        elif not key.isalpha():
            print("Gabim: key duhet te permbaje vetem shkronja.")
        else:
            ciphertext, _, _ = redefence_encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)

    elif choice == 'd':
        ciphertext = input("Shkruaj ciphertext: ")
        key = input("Shkruaj key: ").replace(" ", "").strip()

        if key == "":
            print("Gabim: key nuk mund te jete bosh.")
        elif not key.isalpha():
            print("Gabim: key duhet te permbaje vetem shkronja.")
        else:
            plaintext = redefence_decrypt(ciphertext, key)
            print("Plaintext:", plaintext)

    else:
        print("Zgjedhje jo valide!")

else:
    print("Algoritmi jo valid!")