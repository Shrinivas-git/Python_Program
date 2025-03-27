def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution completed.")


print("Case 1: Division by a non-zero number")
divide_numbers(10, 2)

print("\nCase 2: Division by zero")
divide_numbers(10, 0)
