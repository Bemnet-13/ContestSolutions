from collections import Counter
test = int(input())
checker = Counter('Timur')

for i in range(test):
    length = int(input())
    string = input()
    c = Counter(string)
    if checker == c:
        print('YES')
    else:
        print('NO')

