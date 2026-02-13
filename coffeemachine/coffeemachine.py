class CoffeeMachine:

    def init(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money\n")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()

        if choice == "back":
            return

        if choice == "1":
            water = 250
            milk = 0
            beans = 16
            cost = 4
        elif choice == "2":
            water = 350
            milk = 75
            beans = 20
            cost = 7
        elif choice == "3":
            water = 200
            milk = 100
            beans = 12
            cost = 6
        else:
            return

        if self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.beans < beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += cost

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())

        print("Write how many ml of milk you want to add:")
        self.milk += int(input())

        print("Write how many grams of coffee beans you want to add:")
        self.beans += int(input())

        print("Write how many disposable cups you want to add:")
        self.cups += int(input())

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def process(self, command):

        if command == "buy":
            self.buy()

        elif command == "fill":
            self.fill()

        elif command == "take":
            self.take()

        elif command == "remaining":
            self.print_state()

        elif command == "exit":
            return False

        return True


machine = CoffeeMachine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    command = input()

    if not machine.process(command):
        break