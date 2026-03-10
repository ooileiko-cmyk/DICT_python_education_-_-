import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

type_ = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

if interest is None:
    print("Incorrect parameters")
    exit()

i = interest / (12 * 100)

if type_ == "diff":
    if payment is not None or principal is None or periods is None:
        print("Incorrect parameters")
    else:
        total = 0
        for m in range(1, periods + 1):
            d = math.ceil(principal / periods + i * (principal - (principal * (m - 1) / periods)))
            total += d
            print(f"Month {m}: payment is {d}")
        print()
        print(f"Overpayment = {int(total - principal)}")

elif type_ == "annuity":

    if payment is None:
        payment = math.ceil(principal * (i * (1 + i)  periods) / ((1 + i)  periods - 1))
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {payment * periods - principal}")

    elif principal is None:
        principal = payment / ((i * (1 + i)  periods) / ((1 + i)  periods - 1))
        print(f"Your loan principal = {int(principal)}!")
        print(f"Overpayment = {int(payment * periods - principal)}")

    elif periods is None:
        periods = math.log(payment / (payment - i * principal), 1 + i)
        periods = math.ceil(periods)

        years = periods // 12
        months = periods % 12

        if years > 0 and months > 0:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years > 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {months} months to repay this loan!")

        print(f"Overpayment = {int(payment * periods - principal)}")

else:
    print("Incorrect parameters")