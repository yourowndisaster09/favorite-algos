import time

class SegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.ST = [None for _ in range(4 * self.n)]
        self._build(a, 0, self.n - 1, 1)

    def _build(self, a, left, right, st_i):
        if left == right:
            self.ST[st_i] = a[left]
        else:
            mid = ((right - left) // 2) + left
            sumLeft = self._build(a, left, mid, 2 * st_i)
            sumRight = self._build(a, mid + 1, right, (2 * st_i) + 1)
            self.ST[st_i] = sumLeft + sumRight

        return self.ST[st_i]

    def sum(self, qLeft, qRight):
        return self._sum(1, 0, self.n - 1, qLeft, qRight)

    def _sum(self, st_i, boundLeft, boundRight, qLeft, qRight):
        if qLeft <= boundLeft and qRight >= boundRight:
            return self.ST[st_i]

        mid = ((boundRight - boundLeft) // 2) + boundLeft

        if qLeft <= mid:
            leftContribute = self._sum(2 * st_i, boundLeft, mid, qLeft, qRight)
        else:
            leftContribute = 0
        if qRight > mid:
            rightContribute = self._sum((2 * st_i) + 1, mid + 1, boundRight, qLeft, qRight)
        else:
            rightContribute = 0

        return leftContribute + rightContribute

    def update(self, i, val):
        self._update(1, 0, self.n - 1, i, val)

    def _update(self, st_i, boundLeft, boundRight, i, val):
        if boundLeft == boundRight and boundLeft == i:
            diff = val - self.ST[st_i]
            self.ST[st_i] = val
            return diff

        mid = ((boundRight - boundLeft) // 2) + boundLeft
        if i <= mid:
            diff = self._update(2 * st_i, boundLeft, mid, i, val)
        else:
            diff = self._update((2 * st_i) + 1, mid + 1, boundRight, i, val)

        self.ST[st_i] += diff
        return diff


mySegmentTree = SegmentTree([1, 3, -2, 8, -7])
print(mySegmentTree.ST)
print(mySegmentTree.sum(1, 3))
mySegmentTree.update(1, 0)
print(mySegmentTree.sum(1, 3))