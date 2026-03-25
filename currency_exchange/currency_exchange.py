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


    if name == "main":
        print("=== Этап 2 ===")
        stage2()