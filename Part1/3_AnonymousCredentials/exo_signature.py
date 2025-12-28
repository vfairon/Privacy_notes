# I did the exo in python cli and retranscripted it using ChatGPT

# Parameters
p = 47
q = 23
g = 17

print("Public parameters:")
print("p =", p)
print("q =", q)
print("g =", g)
print()

u0 = 42
u1 = 37

m1 = 22
r = 2
x = 17

print("Secrets:")
print("m1 =", m1)
print("r  =", r)
print("x  =", x)
print()

# Commitment
c = (pow(u1, m1, p) * pow(u0, r, p)) % p
d = pow(c, x, p)
h = pow(g, x, p)

print("Commitment and keys:")
print("c =", c)
print("d =", d)
print("h =", h)
print()

# Signer randomness
R = 3
a = pow(g, R, p)
b = pow(c, R, p)
a0 = pow(u0, R, p)

print("Signer randomness:")
print("R  =", R)
print("a  =", a)
print("b  =", b)
print("a0 =", a0)
print()

# Re-randomization parameters
rp = 12
w = 11
Rp = 6

print("Re-randomization:")
print("rp =", rp)
print("w  =", w)
print("Rp =", Rp)
print()

# Re-randomized commitment
cp = (c * pow(u0, rp, p)) % p
v0 = pow(u0, x, p)
dp = (d * pow(v0, rp, p)) % p

print("Re-randomized commitment:")
print("c' =", cp)
print("v0 =", v0)
print("d' =", dp)
print()

# Re-randomized proof elements
ap = (pow(a, w, p) * pow(g, Rp, p)) % p

bp = (
    pow((b * pow(a0, rp, p)) % p, w, p) *
    pow((c * pow(u0, rp, p)) % p, Rp, p)
) % p

print("Re-randomized proof:")
print("a' =", ap)
print("b' =", bp)
print()

# Challenge
ep = 7
w_inv = pow(w, q - 2, q)
e = (ep * w_inv) % q

print("Challenge:")
print("e' =", ep)
print("w^-1 =", w_inv)
print("e  =", e)
print()

# Schnorr responses (CORRECT FORMULA)
f = (R + e * x) % q
fp = (Rp + w * f) % q

print("Responses:")
print("f  =", f)
print("f' =", fp)
print()

# Verifications
left1 = pow(g, fp, p)
right1 = (ap * pow(h, ep, p)) % p

left2 = pow(cp, fp, p)
right2 = (bp * pow(dp, ep, p)) % p

print("Verification 1 (knowledge of x):")
print("g^f' =", left1)
print("a' * h^e' =", right1)
print("OK ?", left1 == right1)
print()

print("Verification 2 (binding to commitment):")
print("c'^f' =", left2)
print("b' * d'^e' =", right2)
print("OK ?", left2 == right2)
print()

assert left1 == right1
assert left2 == right2

print("✔ All checks passed")
