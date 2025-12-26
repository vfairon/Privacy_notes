p = 17
g = 3
print(f"(p, g) = ({p}, {g})")
G = []

e = g
while e != 1:
    G.append(e)
    e = (e * g) % p
G.append(1)
print(f"G = {G}")

def CDH(g, g_x, g_y):
    g_x = g_x % p
    g_y = g_y % p
    i = j = -1
    for k in range(len(G)):
        if g_x == G[k]:
            i = k + 1
        if g_y == G[k]:
            j = k + 1
    return pow(g, i * j, p)

assert CDH(g, g**2, g**3) == pow(g, 2 * 3, p)

def DL(g, h):
    h = h % p
    for x in range(1, p):
        if CDH(g, g**x, g**1) == h:
            return x
    return -1

assert DL(g, g**2) == 2
for i in range(len(G)):
    assert DL(g, G[i]) == i + 1
