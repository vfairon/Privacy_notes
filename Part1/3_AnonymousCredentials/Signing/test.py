from random import randint

use_additive_diversion = True

p = 47
g = 17

q = 0
G = []

while True:
    elem = g**(q + 1) % p
    q += 1
    G.append(elem)
    if elem == 1:
        break

print("(p, g, q) =", (p, g, q))
print("G =", G)

# P side
print("P computes :")
x = randint(1, q - 1)
h = g**x % p
print("keys (x, h) =", (x, h))
print("P publishes h to D and V")

print("P computes and send to D :")
y = randint(1, q - 1)
a = g**y % p
print("(y, a) =", (y, a))

# D side
print("D computes and send to V :")
w = randint(1, q - 1)
yp = randint(1, q - 1)

if use_additive_diversion:
    ap = a * g**yp * h**w % p
else:
    ap = a**w * g**yp % p

print("(w, yp, ap) =", (w, yp, ap))

# V side
print("V computes and send to D :")
ep = randint(1, q - 1)
print("ep =", ep)

# D side
print("D computes and send to P :")

if use_additive_diversion:
    e = (ep + w) % q
    print("e =", e)
else:
    for w_1 in range(1, p):
        if w * w_1 % q == 1: # Modulo q here because w is part of an exponent
            break
    e = (ep * w_1) % q
    print("(w_1, e) =", (w_1, e))

# P side
print("P computes and send to D :")
z = (e * x + y) % q
print("z =", z)

# D side
print("D checks that h**e * a % p == g**z % p")
left = h**e * a % p
right = g**z % p
print("(h**e * a % p, g**z % p, check) =", (left, right, left == right))

print("D computes and sends to V :")

if use_additive_diversion:
    zp = (z + yp) % q
else:
    zp = (w * z + yp) % q
print("zp =", zp)

# V side
print("V checks that h**ep * ap % p == g**zp % p")
left = (h**ep * ap) % p
right = (g**zp) % p
print("(h**ep * ap % p, g**zp % p, check) =", (left, right, left == right))