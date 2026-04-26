text=input("enter text:")
shift=int(input("shift:"))

enc=""

for c in text:
    if c.isalpha():
        base= 65 if c.isupper() else 97
        enc+=chr((ord(c)-base+shift)%26+base)
    else:
        enc+=c

dec="" 

for c in enc:
    if c.isalpha():
        base= 65 if c.isupper() else 97
        dec+= chr((ord(c)-base-shift)%26+base)
    else:
        dec+=c
print("Encrypted:",enc)
print("Decrypted:",dec)