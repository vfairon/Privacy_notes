from random import randint

p = 47
g = 17
q = 23
print("(p, g, q) =", (p, g, q))

x1 = 8
x2 = 2
x3 = 19
print("(x1, x2, x3) =", (x1, x2, x3))

h1 = g**x1 % p
h2 = g**x2 % p
h3 = g**x3 % p
print("(h1, h2, h3) =", (h1, h2, h3))

h = h1 * h2 * h3 % p
print("h =", h)

# Sender S (external)
r = 17
m = 16
c1 = g**r % p
c2 = m * h**r % p
print("(r, m, c1, c2) =", (r, m, c1, c2))

# Trustees compute their partial decryption
# And share it securely to each other
d1 = c1**x1 % p
d2 = c1**x2 % p
d3 = c1**x3 % p
print("(d1, d2, d3) =", (d1, d2, d3))

# Trustees decrypt
d = d1 * d2 * d3 % p
for d_1 in range(1, p):
    if d * d_1 % p == 1:
        break
dec_m = c2 * d_1 % p
print("(d, d_1, dec_m) =", (d, d_1, dec_m))
