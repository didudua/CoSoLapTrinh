def longest_common_substring(A, B):
    m = len(A)
    n = len(B)
    DP = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])
    C = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            C = A[i - 1] + C
            i -= 1
            j -= 1
        elif DP[i][j - 1] > DP[i - 1][j]:
            j -= 1
        else:
            i -= 1

    return C

A = input()
B = input()

C = longest_common_substring(A, B)
print(len(C))
