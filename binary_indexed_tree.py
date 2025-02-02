# AKA Fenwick Tree
class BIT:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = [0 for _ in range(self.n)]
        self.bit = [0 for _ in range(self.n + 1)]
        for i, val in enumerate(arr):
            self.update(i, val)

    def update(self, i, val):
        diff = val - self.arr[i]
        self.arr[i] = val
        b = i + 1
        while b <= self.n:
            self.bit[b] += diff
            b += b & -b

    def search(self, left, right):
        r = right + 1
        sumFromZeroInclusive = 0
        while r > 0:
            sumFromZeroInclusive += self.bit[r]
            r -= r & -r

        l = left
        sumToLeftExclusive = 0
        while l > 0:
            sumToLeftExclusive += self.bit[l]
            l -= l & -l

        return sumFromZeroInclusive - sumToLeftExclusive


myBit = BIT([3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3])

print(myBit.bit)
assert(myBit.search(0, 10) == 31)
assert(myBit.search(1, 3) == 7)
assert(myBit.search(5, 9) == 13)