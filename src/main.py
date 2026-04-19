from redefence_cipher import redefence_encrypt, redefence_decrypt

choice = input("Zgjedh (E)ncrypt ose (D)ecrypt: ").lower()

if choice == 'e':
    plaintext = input("Shkruaj plaintext: ")
    key = input("Shkruaj key: ").replace(" ", "").strip()

    if key == "":
        print("Gabim: key nuk mund te jete bosh.")
    elif not key.isalpha():
        print("Gabim: key duhet te permbaje vetem shkronja.")
    else:
        ciphertext, _, _ = redefence_encrypt(plaintext, key)
        print("\nCiphertext:", ciphertext)

elif choice == 'd':
    ciphertext = input("Shkruaj ciphertext: ")
    key = input("Shkruaj key: ").replace(" ", "").strip()

    if key == "":
        print("Gabim: key nuk mund te jete bosh.")
    elif not key.isalpha():
        print("Gabim: key duhet te permbaje vetem shkronja.")
    else:
        plaintext = redefence_decrypt(ciphertext, key)
        print("\nPlaintext:", plaintext)

else:
    print("Zgjedhje jo valide!")