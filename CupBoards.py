n = int(input())
left = []
right = []

for _ in range(n):
    l, r = map(int,input().split())
    left.append(l)
    right.append(r)

open_left = left.count(1)
closed_left = len(left) - open_left
open_right = right.count(1)
closed_right = len(right) - open_right 

ans = min(open_left,closed_left) + min(open_right, closed_right)
print(ans)