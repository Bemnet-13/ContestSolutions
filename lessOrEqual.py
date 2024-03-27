n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
i = k - 1
if i == -1 and arr[0] > 1:
    print(1)
elif n == k or arr[i] != arr[k]:
    print(arr[i])
else:
    print(-1)