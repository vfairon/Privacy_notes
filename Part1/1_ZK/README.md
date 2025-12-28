Note modulo p is always done on 'normal values' sent as we work with numbers in Zq so when you send datas implicitly it applicates mod p on everything.
But there is an exception when we compute value destinated to be exponent as e and f in general, we applicate a modulo q on it.

Recall with have an order prime p and a generator prime g so G[i] = g**i % p
G is a cyclic set with q elements and q is a prime also.

I think when you do :
a**x % p with x > p, q it's equal to a**(x % q) % p automatically that's why it's often not explicit
