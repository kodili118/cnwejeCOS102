# A program to calculate the Annual Tax Revenue(ATR) of a worker in Izifin Technology

print("Welcome to Izifin Technology")

# User input
experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))

# Determine Annual Tax Revenue (ATR)
if experience > 25 and age >= 55:
    atr = ("5600000")  #5,600,000
elif experience > 20 and age >= 45:
    atr = ("4480000")  #4,480,000
elif experience > 10 and age >= 35:
    atr = ("1500000")  #1,500,000
else:
    atr = ("550000")  #550,000 

# Output ATR
print(f"Annual Tax Revenue (ATR): {atr}")