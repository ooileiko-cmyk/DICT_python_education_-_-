# Этап 1: простая конвертация
def stage1():
    mycoin = float(input("Введите количество ваших mycoins: "))
    rate = float(input("Введите обменный курс (mycoin -> USD): "))
    total = mycoin * rate
    print(f"Общая сумма в долларах: {total:.2f}\n")

if name == "main":
    print("=== Этап 1 ===")
    stage1()


    # Этап 2: конвертация в несколько валют
    def stage2():
        mycoin = float(input("Введите количество ваших mycoins: "))

        rates = {
            "HNL": 0.17,
            "ARS": 0.82,
            "MAD": 0.208,
            "AUD": 1.9622
        }

        for currency, rate in rates.items():
            total = round(mycoin * rate, 2)
            print(f"Вы получите {total} {currency} от продажи {mycoin} mycoins.")

import requests


def stage3():
    base_currency = input("Введите код вашей валюты (например, USD, EUR): ").upper()
    url = f"http://www.floatrates.com/daily/{base_currency.lower()}.json"
    response = requests.get(url)
    data = response.json()

    for target in ["usd", "eur"]:
        if target in data:
            print(f"Курс {target.upper()} к {base_currency}: {data[target]['rate']}")


if name == "main":
    print("=== Этап 3 ===")
    stage3()