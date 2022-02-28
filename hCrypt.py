# ██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
# ██║  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
# ███████║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║
# ██╔══██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║
# ██║  ██║╚██████╗██║  ██║   ██║   ██║        ██║
# ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝
from hashlib import sha256

print("Welcome to the hCrypt simple cryptage script.")

enter = input("Enter the name of the file to be encrypted/decrypted: ")
output = input("Enter the name of the final file: ")
key = input("Enter cryptage key: ")
keys = sha256(key.encode('utf-8')).digest()
with open(enter,'rb') as f_enter:
    with open(sortie,'wb') as f_output:
        i = 0
        while f_enter.peek():
            c = ord(f_enter.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_output.write(b)
            i = i + 1