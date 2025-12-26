from random import randint
from sympy import discrete_log

# P and V
p = 47
g = 17
G = []
elem = g
while elem != 1:
    G.append(elem)
    elem = (elem * g) % p
G.append(1)
q = len(G)
print(f"(p, g, q) = {(p, g, q)}")
print(f"G = {G}")

def inverse(y: int, p: int):
    return pow(y, p - 2, p)

# V
x = G[2]
h = pow(g, x, p)
print(f"x = {x}, h = {h}")

# P
v = randint(0, 1)
r = randint(0, q - 1)
c = (
    pow(g, r, p),
    pow(g, v, p) * pow(h, r, p) % p
)
print(f"v = {v}, r = {r}, c = {c}")

a = [[0, 0], [0, 0]]
e = [0, 0]
f = [0, 0]

e[1 - v] = randint(0, q - 1)
f[1 - v] = randint(0, q - 1)
a[1 - v][0] = pow(g, f[1 - v], p) * pow(inverse(c[0], p), e[1 - v], p) % p
tmp = c[1] * inverse(pow(g, v, p), p) % p
a[1 - v][1] = pow(h, f[1 - v], p) * pow(inverse(tmp, p), e[1 - v], p) % p


rp = randint(0, q - 1)
a[v][0] = pow(g, rp, p)
a[v][1] = pow(h, rp, p)
print(f"rp = {rp}")
print(f"a[{v}] = {a[v]}, a[{1 - v}] = {a[1 - v]}")

# V
E = randint(0, q - 1)
print(f"E = {E}")

# P
e[v] = (E - e[1 - v]) % q
f[v] = (rp + r * e[v]) % q

print(f"e[{v}] = {e[v]}, e[{1 - v}] = {e[1 - v]}")
print(f"f[{v}] = {f[v]}, f[{1 - v}] = {f[1 - v]}")

# V
g_v = c[1] * inverse(pow(c[0], x, p), p) % p
print(f"g_v = {g_v}, discrete_log(g, g_v, p) = {discrete_log(p, g_v, g)}")
print(f"E ?= e[0] + e[1] <=> {E == (e[0] + e[1]) % q}")
for i in range(0, 2, 1):
    print(f"g**f[{i}] ?= a[{i}][0] * c[0]**e[{i}] % p <=> {pow(g, f[i], p) == a[i][0] * pow(c[0], e[i], p) % p}")
    print(f"h**f[{i}] ?= a[{i}][1] * (c[1] * g_v**-1)**e[{i}] % p <=> {pow(h, f[i], p) == a[i][1] * pow((c[1] * inverse(g_v, p)), e[i], p) % p}")
