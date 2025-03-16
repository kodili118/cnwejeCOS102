def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    A = P * (1 + (R / n))** (n * t)
    return A

def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + (R / n)) ** (n * t) - 1) / (R / n))
    return A

# User input
print ("Select a calculation:")
print("1. Simple Interest")
print("2. Compound Interst")
print("3. Annuity Plan")
choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    P = float(input("Enter Principal Amount: "))
    R = float(input("Enter Rate of Interest (in %): "))
    T = float(input("Enter Time Period (years): "))
    print(f"Simple Interest Amount: {simple_interest(P, R, T):.2f}")

elif choice ==2:
    P = float(input("Enter Principal Amount: "))
    R = float(input("Enter Rate of Interest (in %): "))
    n = int(input("Enter Number of Times Interest is Compounded Per Year: "))
    t = float(input("Enter the Time Period (years): "))
    print(f"Compound Interest Amount: {compound_interest(P, R, n, t):.2f}")

elif choice ==3:
    PMT = float(input("Enter Payment Amount: "))
    R = float(input("Enter Rate of Interest (in %): "))
    n = int(input("Enter Number of Times Interest is Compounded Per Year: "))
    t = float(input("Enter Time Period (years): "))
    print(f"Annuity Plan Amount: {annuity_plan(PMT, R, n, t):.2f}")

else:
    print("Invalid choice! Please select 1, 2, or 3.")