N = int(input())

for i in range(N):
    for _ in range(N - i):
        print("*", end="")
    print()