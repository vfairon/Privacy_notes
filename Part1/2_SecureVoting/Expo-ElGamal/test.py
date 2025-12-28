from random import randint
from sympy.ntheory import discrete_log

# Common shared infos
p = 47
g = 17
q = 23
# Define group G
print("(p, g, q) =", (p, g, q))

# From Entiry
x = randint(1, q - 1)
h = g**x % p
# Publishes h
print("(x, h) =", (x, h))

# From voters
N = 10
voters = []
sum = 0
for i in range(N):
    m = randint(0, 1)
    sum += m
    mp = g**m % p
    r = randint(1, q - 1) # Exponent so mod q
    c1 = g**r % p
    c2 = mp * h**r% p
    print(f"{i} => (m, mp, r, c1, c2) = ({m}, {mp}, {r}, {c1}, {c2})")
    # Publishes (c1, c2)
    voters.append((c1, c2))

# From entity
c1_mul = 1
c2_mul = 1

i = 0
for c1, c2 in voters:
    c1_mul *= c1
    c2_mul *= c2

    # Entity sneak
    def sneak():
        s = c1**x % p
        for s_1 in range(1, p):
            if s * s_1 % p == 1:
                break
        mp = c2 * s_1 % p
        m = discrete_log(p, mp, g)
        return m
    print(f"Entity sneak => voter {i} voted {sneak()}")

print("(c1_mul, c2_mul) =", (c1_mul, c2_mul))

s = c1_mul**x % p
for s_1 in range(1, p):
    if s * s_1 % p == 1:
        break

print("(s, s_1) =", (s, s_1))

mp_mul = c2_mul * s_1 % p
print("mp_mul =", mp_mul)

# log_g(mp_mul) % p
m_sum = discrete_log(p, mp_mul, g)
print("(sum, m_sum) =", (sum, m_sum))

# The utility of this algorithm isn't about security but about performance
# The multiplication of exponential votes give the exponential of sum of votes
# then it can be decrypted with discrete log
# This is much easier than compute a discrete log one by one on each user encryption
# So just multiply all encryptions and decrypts it ones but to make it work it's for
# what we bothers to send encrypted exponential of votes
