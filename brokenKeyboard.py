tests = int(input())

for _ in range(tests):
    s = input()
    stack = [s[0]]  
    for i in range(1, len(s)):  
        if stack and stack[-1] == s[i]:  # Check if stack is not empty before accessing stack[-1]
            stack.pop()
        else:
            stack.append(s[i])
    
    print(''.join(stack))