from random import randint as rint
from time import sleep
key = rint(0, 9999)
def encrypt(message):
    encrypted = ""
    for char in message:
        encrypted += hex(ord(char) ^ key)[2:].zfill(4)
    return encrypted
def decrypt(encrypted, key):
    decrypted = ""
    for i in range(0, len(encrypted), 4):
        decrypted += chr(int(encrypted[i:i+4], 16) ^ key)
    return decrypted
choice = input("Do you want to encrypt or decrypt text? (e/d): ")
if choice.lower() == "e":
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(message)
    print("Encrypted message:", encrypted)
    print("Key:", key)
    sleep(60)
elif choice.lower() == "d":
    encrypted = input("Enter a message to decrypt: ")
    key = int(input("Enter the key: "))
    decrypted = decrypt(encrypted, key)
    print("Decrypted message:", decrypted)
    sleep(60)
