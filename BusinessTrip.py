k = int(input())

growth_rate = list(map(int, input().split()))
growth_rate.sort(reverse=True)

growth = 0
if k == 0:
    print(growth)
elif sum(growth_rate) < k:
    print(-1)
else:
    for i in range(len(growth_rate)):
        growth += growth_rate[i]
        if growth >= k:
            print(i+1)
            break
