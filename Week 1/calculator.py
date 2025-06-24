def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    if b == 0:
        return "Error: Division by zero."
    return a / b

def calculator():
    print("\n=== Interactive Calculator ===")
    print("Enter an operation: add, sub, mul, div or 'exit' to quit.")
    while True:
        op = input("\nOperation: ").lower().strip()
        if op == "exit":
            print("👋 Exiting the calculator. Bye!")
            break
        if op not in ["add", "sub", "mul", "div"]:
            print("❌ Invalid operation. Try again.")
            continue
        
        try:
            a = float(input("Enter the first number: ").strip())
            b = float(input("Enter the second number: ").strip())
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        if op == "add":
            result = add(a, b)
        elif op == "sub":
            result = sub(a, b)
        elif op == "mul":
            result = mul(a, b)
        else:
            result = div(a, b)

        print(f"✅ Result: {result}")

if __name__ == "__main__":
    calculator()
