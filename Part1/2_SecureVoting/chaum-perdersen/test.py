from random import randint

p = 47
g = 17

def generate_group(p, g):
    G = []
    for i in range(1, 100000000):
        t = g**i % p
        G.append(t)
        if t == 1:
            break
    return G

G = generate_group(p, g)
q = len(G)

def find_other_generator(p, g, q):
    t = randint(1, q - 1)
    return g**t % p

print("(p, g, q) =", (p, g, q))
print("G =", G)

gp = find_other_generator(p, g, q)
Gp = generate_group(p, gp)
qp = len(Gp)
print("(p, gp, qp) =", (p, gp, qp))
print("Gp =", Gp)

print("G vs Gp")
print("sort(G) =", sorted(G))
print("sort(Gp) =", sorted(Gp))
