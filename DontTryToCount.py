t = int(input())

def minOperations(n,m,x,s):
    ops = 0
    while True:
        if x.find(s) != -1:
            return ops
        else:
            x = x + x
            ops += 1
        if x.find(s) == -1 and ops > 1:
            if len(x) > len(s):
                return -1

for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    res = minOperations(n,m,x,s)
    print(res)
