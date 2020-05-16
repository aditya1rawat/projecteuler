# # # Problem 001: Multiples of 3 & 5 # # #

ans = []
x = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        ans.append(x)

print(sum(ans))