# Get a number from the user
num = int(input("Enter a number: "))

# Check if the number is zero
if num == 0:
    print("The number is zero.")
# Check if the number is even
elif num % 2 == 0:
    print("The number is even.")
# If it's not zero and not even, it must be odd
else:
    print("The number is odd.")
