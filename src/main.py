from autokey import autokey_encrypt, autokey_decrypt

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
