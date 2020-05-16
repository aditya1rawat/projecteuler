# # # Problem 002: Even Fibonacci Numbers # # #
n1 = 0
n2 = 1
seq_list = [0]
limit = 4000000

while seq_list[-1] < limit:
    total = n1 + n2
    n1 = n2
    n2 = total
    if n2 % 2 == 0:
        seq_list.append(n2)


seq_list.pop()
print(seq_list)
print(sum(seq_list))