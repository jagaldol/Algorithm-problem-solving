def compute_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_pi(pattern)
    result = []
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                result.append(i - m + 2)  # 1-based index
                j = pi[j]
            else:
                j += 1
    return result


text = input().rstrip()
pattern = input().rstrip()

positions = kmp(text, pattern)
print(len(positions))
print(" ".join(map(str, positions)))
