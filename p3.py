# # # Problem 003: Largest Prime Number # # #

num = 600851475143  
result = 2

while num > result:
    if num % result == 0:
        num /= result
    result += 1

print(result)