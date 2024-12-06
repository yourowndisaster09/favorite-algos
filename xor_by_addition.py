def xor_by_addition(a, b):
    sums = [0 for _ in range(32)]
    i = 0
    while a or b:
        sums[i] += (a & 1) + (b & 1)
        a >>= 1
        b >>= 1
        i += 1
    mod = [x % 2 for x in sums]
    c = 0
    for bit in reversed(mod):
        c <<= 1
        c |= bit
    return c

assert(xor_by_addition(8, 3) == 8^3)
assert(xor_by_addition(23, 41) == 23^41)