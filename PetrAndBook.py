n = int(input())
days = list(map(int, input().split()))

completed = 0
i = 0
total = 0

while True:
    completed += days[i]
    total += 1
    i += 1
    if i == len(days):
        i = 0
    if completed >= n:
        if total % 7 == 0:
            print(7)
        else:
            print(total % 7)
        break