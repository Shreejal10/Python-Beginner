n = int(input("Enter a number: "))
value = n  # store the input in a variable
sum = 0
order = len(str(n))

while (n > 0):
    digit = n % 10
    sum += digit ** order
    n = n//10

if sum == value:
    print(f"{value} is an Armstrong number")

else:
    print(f"{value} is not an Armstrong number")
