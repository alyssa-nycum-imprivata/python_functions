def calc_dollars(**coins):
    dollarAmount = 0

    for key, value in coins.items():
        if key == "pennies":
            pennyAmount = value / 100
            dollarAmount += pennyAmount
        elif key == "nickels":
            nickleAmount = value / 20
            dollarAmount += nickleAmount
        elif key == "dimes":
            dimeAmount = value / 10
            dollarAmount += dimeAmount
        elif key == "quarters":
            quarterAmount = value / 4
            dollarAmount += quarterAmount

    print(dollarAmount)


calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)