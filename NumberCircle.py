n = int(input())
arr = list(map(int, input().split()))

arr.sort()
# Use two pointers

if arr[-1] >= arr[-2] + arr[-3]:
    print('NO')
else:
    print('YES')
    for i in range(n-1, -1, -2):
        print(arr[i], end = " ")
    for i in range(n % 2, n, 2):
        print(arr[i], end = " ")














# arr[-1], arr[-2] = arr[-2], arr[-1]
# l = -2
# r = 0
# tri = True

# while r < n:
#     mid = (l + r) // 2
#     if arr[l] + arr[r] <= arr[mid]:
#         tri = False
#         break
#     l += 1
#     r += 1

# if not tri:
#     print('NO')
# else:
#     print('YES')
#     arr  = [str(num) for num in arr]
#     print(' '.join(arr))