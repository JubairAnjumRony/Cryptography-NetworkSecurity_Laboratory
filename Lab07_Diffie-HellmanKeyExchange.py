p=23
g=5

a=44 # alice private key
b=15 # bobs private kye

# key generated

x= pow(g,a,p)
y=pow(g,b,p)

#shared secret key

Ka=pow(y,a,p)
Kb=pow(x,b,p)

print(" Secret key for Alice:",Ka)
print(" Secret key for Bob:",Kb)