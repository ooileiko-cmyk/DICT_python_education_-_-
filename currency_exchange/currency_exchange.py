# Этап 1: простая конвертация
def stage1():
    mycoin = float(input("Введите количество ваших mycoins: "))
    rate = float(input("Введите обменный курс (mycoin -> USD): "))
    total = mycoin * rate
    print(f"Общая сумма в долларах: {total:.2f}\n")

if name == "main":
    print("=== Этап 1 ===")
    stage1()