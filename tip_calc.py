# Problme set O from cs50


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(bill):
    #convert str input into float and return to dollars.
    bill = bill.replace('$', '')
    bill = float(bill)
    return round(bill, 1)

def percent_to_float(tip_amount):
    # drop % sign
    tip_amount = tip_amount.replace("%", "")
    # convert str to a float
    tip_amount = float(tip_amount) / 100
    return tip_amount

main()