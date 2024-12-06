# Longest increasing subsequence
# Example
# 5 7 4 -3 9 1 10 4 5 8 9
#
#       -3   1    4 5 8 9 --> Length 6
# 5 7      9   10         --> Length 4
# 5                   8 9 --> Length 3
#     4    9   10         --> Length 3
#              10         --> Length 1
#
# From left to right, if end is included:
# 5                       -> 1 (5)
# 5 7                     -> 2 (5 7)
# 5 7 4                   -> 1 (4)
# 5 7 4 -3                -> 1 (-3)
# 5 7 4 -3 9              -> 3 (5 7 9)
# 5 7 4 -3 9 1            -> 2 (-3 1)
# 5 7 4 -3 9 1 10         -> 4 (5 7 9 10)
# 5 7 4 -3 9 1 10 4       -> 3 (-3 1 4)
# 5 7 4 -3 9 1 10 4 5     -> 4 (-3 1 4 5)
# 5 7 4 -3 9 1 10 4 5 8   -> 5 (-3 1 4 5 8)
# 5 7 4 -3 9 1 10 4 5 8 9 -> 6 (-3 1 4 5 8 9)
# MAX = 6
# O(n^2)
def solve(A):
    L = [None] * len(A)
    for i in range(len(A)):
        prevMax = 0
        for j in range(i):
            if A[j] < A[i] and L[j] > prevMax:
                prevMax = L[j]
        L[i] = 1 + prevMax
    return max(L)

print(solve([5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9]))




