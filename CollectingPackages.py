t = int(input())

for _ in range(t):
    p = int(input())
    coordinates = [[0, 0]]
    moves = ""
    result = True

    
    for i in range(p):
        x, y = list(map(int, input().split()))
        coordinates.append([x, y])
    coordinates.sort()

    for i in range(1, p + 1):
        if coordinates[i][0] == coordinates[i-1][0]:
            moves += 'U' * (coordinates[i][1] - coordinates[i-1][1])
        elif coordinates[i][1] == coordinates[i-1][1]:
            moves += 'R' * (coordinates[i][0] - coordinates[i-1][0])
        elif coordinates[i][0] > coordinates[i-1][0] and coordinates[i][1] > coordinates[i-1][1]:
            moves += 'R' * (coordinates[i][0] - coordinates[i-1][0]) + 'U' * (coordinates[i][1] - coordinates[i-1][1])
        else:
            result = False
            break
    if not result:
        print('NO')
    else:
        print('YES')
        print(moves)