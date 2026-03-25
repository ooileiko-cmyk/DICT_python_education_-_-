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
    import os
    import json
    import requests

    CACHE_DIR = "cache_currency"
    os.makedirs(CACHE_DIR, exist_ok=True)


    def stage4():
        base_currency = input("Введите валюту для обмена (код): ").upper()
        target_currency = input("Введите валюту, на которую хотите обменять (код): ").upper()
        amount = float(input("Введите сумму: "))

        cache_file = os.path.join(CACHE_DIR, f"{base_currency}.json")

        if os.path.exists(cache_file):
            print("Проверяем кэш... Это в кэше!")
            with open(cache_file, "r") as f:
                data = json.load(f)
        else:
            print("Проверяем кэш... Извините, файла нет в кэше!")
            url = f"http://www.floatrates.com/daily/{base_currency.lower()}.json"
            response = requests.get(url)
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)

        if target_currency.lower() in data:
            rate = data[target_currency.lower()]["rate"]
            total = round(amount * rate, 2)
            print(f"Вы получили {total} {target_currency}.")
        else:
            print(f"Курс для {target_currency} не найден.")


    if name == "main":
        print("=== Этап 4 ===")
        stage4()