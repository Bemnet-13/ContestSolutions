# Check if the package coordinates sorting is similar wither with x or y coordinate
# Use a while loop to iterate through the packages
# Use x and y coordinate pointers to locate the current position of the package
# concatenate x * 'R' + y * 'U' to the path string

tests = int(input())

def path_finder(p, packages):

    
    x_sorted = sorted(packages, key = lambda coor: coor[0])
    y_sorted = sorted(packages, key = lambda coor: coor[1])
    if x_sorted[-1] != y_sorted[-1]:
        print('NO')
    else:
        x = y = 0
        path = ''
        for i in range(len(y_sorted)):
            if i == 0:
                x = y_sorted[i][0]
                y = y_sorted[i][1]
            else:
                x = y_sorted[i][0] - y_sorted[i-1][0]
                y = y_sorted[i][1] - y_sorted[i -1][1]
            path += x * 'R' + y * 'U'
        print('YES')
        print(path)

for _ in range(tests):
    p = int(input())
    packages = []
    for _ in range(p):
        xi , yi = map(int, input().split())
        coor = tuple([xi,yi])
        packages.append(coor)
    path_finder(p = p, packages = packages)