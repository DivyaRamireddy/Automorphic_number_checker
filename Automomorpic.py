# automorphic_number_checker.py
# Placement Important Program: AUTOMORPHIC NUMBER ✔️

def is_automorphic(num):
    """
    A number is Automorphic if its square ends with the number itself.
    Example: 25 → 25^2 = 625 (ends with 25)
    """
    square = num * num
    return str(square).endswith(str(num))


if __name__ == "__main__":
    print("🔍 Automorphic Number Checker")
    print("------------------------------")
    
    n = int(input("Enter a number: "))

    if is_automorphic(n):
        print(f"{n} is an Automorphic Number ✔️")
    else:
        print(f"{n} is NOT an Automorphic Number ❌")
