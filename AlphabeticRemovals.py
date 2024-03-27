n, k = map(int, input().split())
s = input()


c = [(s[i], i) for i in range(n)]
c.sort()
c[k:] = sorted(c[k:], key=lambda x: x[1])


result = ''.join(c[i][0] for i in range(k, n))
print(result)




# s_count = Counter(sorted(list(s))[:k])
# res = ""

# for letter in s:
#     if letter in s_count and s_count[letter] <= 0:
#         res += letter
#     elif letter in s_count and s_count[letter] > 0:
#         s_count[letter] -= 1
#     else:
#         res += letter

# print(res)