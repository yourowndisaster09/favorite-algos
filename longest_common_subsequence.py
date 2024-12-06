# Longest common subsequence
# Example
# Array 1 = [B C D B C D A]
#            \  \  |     |
#             \  \  \   /
#              \  \  | |
# Array 2 = [A B E C B A B]
# LCS = 4 (B C B A)

# Rationale:
#   | - A B E C B A B
# --|------------------
# - | 0 0 0 0 0 0 0 0
# B | 0
# C | 0
# D | 0
# B | 0
# C | 0
# D | 0
# A | 0
#
# L[i][j] = LCS for A[0:i] and B[0:j]
# example L[1][1] is for 'B' and 'A' -> since 'B' is not same as 'A', LCS is 0
# example L[1][2] is for 'B' and 'AB' -> LCS is 1, since 'B' and 'B' is the same we add +1 to max LCS of ('' and 'AB') or LCS of ('A' and 'B')
# example L[2][3] is for 'BC' and 'ABD'


def solve(A, B):
    count_A = len(A)
    count_B = len(B)
    # Create m+1 by n+1 matrix
    L = [[0] * (count_B+1) for _ in range(count_A+1)]
    for i in range(1, count_A+1):
        for j in range(1, count_B+1):
            if A[i-1] == B[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    [print(x) for x in L]
    return L[count_A][count_B]

print(solve(['B', 'C', 'D', 'B', 'C', 'D', 'A'], ['A', 'B', 'E', 'C', 'B', 'A', 'B']))
