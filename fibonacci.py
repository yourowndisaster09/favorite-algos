def solve(n):
    T = [None] * (n+1)
    T[0] = 0
    T[1] = 1
    if n < 2:
        return T[n]
    for i in range(2, n+1):
        T[i] = T[i-2] + T[i-1]
    return T[n]



if __name__ == "__main__":
    print(solve(9))