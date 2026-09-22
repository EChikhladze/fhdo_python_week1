num = int(input("Input a number to calculate the factorial: "))
res = 1

while num > 0:
    res *= num
    num -= 1

print("The factorial of " + str(num) + " is: " + str(res))