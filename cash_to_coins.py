import math

dollarAmount = 8.69
cents = dollarAmount * 100
print(cents)

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

piggyBank["quarters"] = math.floor(cents / 25)
cents -= piggyBank["quarters"] * 25

piggyBank["dimes"] = math.floor(cents / 10)
cents -= piggyBank["dimes"] * 10

piggyBank["nickels"] = math.floor(cents / 5)
cents -= piggyBank["nickels"] * 5

piggyBank["pennies"] = math.floor(cents)


print(piggyBank)        
        

