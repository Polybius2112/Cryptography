def encrypt():
    plaintext = input("What message would you like to encrypt? ")
    k = input("What key would you like to use? ")
    ciphertext = []
    for p in plaintext:
        if (((ord(p) + int(k)) % 256) < 32):
            ciphertext.append((ord(p) + int(k) + 224) % 256)
        elif (((ord(p) + int(k)) % 256) >= 32):
            ciphertext.append((ord(p) + int(k)) % 256)
    print("Your encrypted message is: ")
    print("".join(chr(c) for c in ciphertext))
def decrypt():
    ciphertext = input("What message would you like to decrypt? ")
    k = input("What key would you like to use? ")
    plaintext = []
    for c in ciphertext:
        if (((ord(c) - int(k))) < 32):
            plaintext.append(((ord(c) - int(k)) + 224))
        elif (((ord(c) - int(k))) >= 32):
            plaintext.append((ord(c) - int(k)))
    print("Your decrypted message is: ")
    print("".join(chr(p) for p in plaintext))
def main():
    answer = input("Welcome. Enter ''Encrypt'' to encrypt a message or ''Decrypt'' to decrypt a message")
    if (answer.lower().replace(" ", "") == "encrypt"):
        encrypt()
    elif (answer.lower().replace(" ", "") == "decrypt"):
        decrypt()
    else:
        print("Instructions unclear. Please restart the program.")
    transfer = input("Press enter to close the program.")
main()