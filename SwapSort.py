n = int(input())
arr = list(map(int, input().split()))

i = 0
res = []

while i < len(arr):     
    num = max(arr)
    for j in range(i, n):
        if arr[i] > arr[j]:
            num = min(num, arr[j])
    if num != max(arr):
        k = arr.index(num)
        tup = i, k
        arr[i], arr[k] = arr[k], arr[i]
        res.append(tup)
        i += 1
    else:
        i += 1

if len(res) == 0:
    print(0)
else:
    print(len(res))
    for id1, id2 in res:
        print(f"{id1} {id2}")
