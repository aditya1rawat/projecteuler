# # # Problem 004: Largest Palindrome Product # # #

num = 0
for x in range(1000, 100, -1):
    for y in range(x, 100, -1):
        prod = x * y
        if prod > num:
            s = str(x * y)
            if s == s[::-1]:
                num = x * y
print(num)