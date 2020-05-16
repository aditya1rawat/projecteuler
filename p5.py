# # # Problem 005: Smallest Multiple # # #

def check_divide(num):
  for i in range(2,21):
    if num % i != 0:
      return False
  return True

num = 20
while True:
  if check_divide(num):
    break
  else:
    num += 1
print(num)