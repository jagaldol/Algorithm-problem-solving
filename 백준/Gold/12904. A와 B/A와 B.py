S = input()
T = input()


def prev_step(t):
    if t[-1] == "A":
        return t[:-1]
    else:
        return t[:-1][::-1]


while len(T) > len(S):
    T = prev_step(T)

if S == T:
    print(1)
else:
    print(0)
