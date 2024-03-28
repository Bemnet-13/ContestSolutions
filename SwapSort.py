n = int(input())
a = list(map(int, input().split()))


print(n)

for i in range(n):
    pos = i
    for j in range(i + 1, n):
        if a[j] < a[pos]:
            pos = j
    print(i, pos)
    a[i], a[pos] = a[pos], a[i]
