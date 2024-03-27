tests = int(input())

for i in range(tests):
    array1 = []
    array2 = []
    cols = int(input())
    s1 = input()
    s2 = input()
    for j in range(cols):
        count_s1_R = s1.count('R')
        count_s2_R = s2.count('R')
        if s1[j] == 'R':
            array1.append(0)
        else:
            array2.append(1)
        if s2[j] == 'R':
            array1.append(0)
        else:
            array2.append(1)
            
    
    # If the counts of 'R' in both rows are not equal, output 'NO'

    if array1 == array2:
        print('YES')
    else:
        if count_s1_R != count_s2_R:
            print('NO')
        else:
            print('YES')