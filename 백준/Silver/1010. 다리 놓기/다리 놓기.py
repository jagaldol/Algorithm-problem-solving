import math
def main():
    # nCm
    T = int(input())
    for _ in range(T):
        inputRow = input()
        N, M = map(int, inputRow.split(' ')) 
        print(math.comb(M, N))

main()