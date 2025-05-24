# 📐 Factorial Calculator in Python

This is a basic Python program that calculates the **factorial** of a given number using recursion.

---

## 🚀 What It Does

- Takes user input
- Calculates factorial recursively
- Prints the result in a formatted string

---

## 🧠 Key Concepts Used

- Recursion
- Conditional statements
- User input
- Type conversion

---

## 💻 Code Preview

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
