# Simple Fibonacci Series Program

# Number of terms you want
n = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
