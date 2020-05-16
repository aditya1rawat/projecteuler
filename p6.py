# # # Problem 006: Sum Square Difference
sum_of_squares = []

for x in range(101):
    sum_of_squares.append(x*x)

yyyy=sum(sum_of_squares)
print(yyyy)

square_of_sums = 0
for y in range(101):
    square_of_sums += y

print(square_of_sums)
square_the_difference = (square_of_sums * square_of_sums) - yyyy
print(square_the_difference)