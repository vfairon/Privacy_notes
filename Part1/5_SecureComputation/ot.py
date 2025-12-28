from sympy import discrete_log
# discrete_log(p, g_m, g)

p = 47
q = 23
g = 17

# P2
x = 8
b = 0
h = pow(g, x, p)
r = 19
enc_b = (pow(g, r, p), ( pow(g, b, p) * pow(h, r, p) ) % p)
print(f"x = {x}, b = {b}, h = {h}, r = {r}, enc_b={enc_b}")

# P1
m0 = 14
m1 = 16
r0 = 13
r1 = 4
rp = 3
X = enc_b
Y = (pow(X[0], p - 2, p), pow(X[1], p - 2, p))
Z = (pow(g, rp, p), g * pow(h, rp, p) % p)
print(f"m0 = {m0}, m1 = {m1}, r0 = {r0}, r1 = {r1}, rp = {rp}")
print(f"X = {X}, Y = {Y}, Z = {Z}")


c0 = (
	pow(Z[0], m0, p) * pow(Y[0], m0, p) * pow(X[0], r0, p) % p,
	pow(Z[1], m0, p) * pow(Y[1], m0, p) * pow(X[1], r0, p) % p

)
c1 = (
	pow(X[0], m1, p) * pow(Z[0], r1, p) * pow(Y[0], r1, p) % p,
	pow(X[1], m1, p) * pow(Z[1], r1, p) * pow(Y[1], r1, p) % p
)
print(f"c0 = {c0}, c1 = {c1}")

# P2
if b == 0:
    C0 = c0[0]
    C1 = c0[1]
else:
    C0 = c1[0]
    c1 = c1[1]

s = pow(C0, x, p)
s_1 = pow(s, p - 2, p)
sp = C1 * s_1 % p
print(f"s = {s}, s_1 = {s_1}, sp = {sp}")

dec_C0_C1 = discrete_log(p, sp, g)
mb = dec_C0_C1
print(f"mb = {mb}")
