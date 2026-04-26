text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

# Extend key
key = (key * len(text))[:len(text)]

# Encryption
enc = ""
for i in range(len(text)):
    
    p = ord(text[i]) - 65
    k = ord(key[i]) - 65
    enc += chr((p + k) % 26 + 65)

print("Encrypted:", enc)

# Decryption
dec = ""
for i in range(len(enc)):
    
    c = ord(enc[i]) - 65
    k = ord(key[i]) - 65
    dec += chr((c - k) % 26 + 65)   

print("Decrypted:", dec)