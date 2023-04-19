import math

def main():
    # mCn
    # m!/((m-n)! * n!)
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split()) 
        print(math.comb(M, N))

main()