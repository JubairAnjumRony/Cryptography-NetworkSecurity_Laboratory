import math
p=17
q=11

n=p*q
phi=(p-1) * (q-1)

for e in range(2,phi):
    if math.gcd(e,phi)==1:
        break

d=pow(e,-1,phi)

msg=int(input("Enter the message:"))
print(f"n = {n}, φ(n) = {phi}")
print(f"Public key  → (e={e}, n={n})")
print(f"Private key → (d={d}, n={n})")


c=pow(msg,e,n)
print("Encrypted:",c)

decrypted=pow(c,d,n)
print("Decrypted:",decrypted)