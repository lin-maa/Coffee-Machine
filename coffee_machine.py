class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.act = str()

    def ingredient(self, water_need, milk_need, \
                   beans_need, cups_need, money_add):
        if self.water >= water_need and self.milk >= milk_need \
                and self.beans >= beans_need and self.cups >= cups_need:
            print('I have enough resources, making you a coffee!')
            self.water -= water_need
            self.milk -= milk_need
            self.beans -= beans_need
            self.money += money_add
            self.cups -= cups_need
        elif self.water < water_need:
            print('Sorry, not enough water!')
        elif self.milk < milk_need:
            print('Sorry, not enough milk!')
        elif self.beans < beans_need:
            print('Sorry, not enough beans!')
        elif self.cups < cups_need:
            print('Sorry, not enough cups!')

    def __str__(self):
        print("The coffee machine has:")
        print('{} of water'.format(self.water))
        print('{} of milk'.format(self.milk))
        print('{} of coffee beans'.format(self.beans))
        print('{} of disposable cups'.format(self.cups))
        print('{} of money'.format(self.money))
        print()

    def action(self):
        while True:
            user_choice = input('Write action '
                                '(buy, fill, take, remaining, exit):')
            if user_choice == 'buy':
                self.buy()
            if user_choice == 'fill':
                self.fill()
            if user_choice == 'take':
                self.take()
            if user_choice == 'remaining':
                self.__str__()
            if user_choice == 'exit':
                break

    def buy(self):
        coffee_type = input('What do you want to buy? 1 - espresso, '
                            '2 - latte, 3 - cappuccino, back - to main menu:')
        if coffee_type == 'back':
            return
        elif coffee_type == '1':
            self.ingredient(250, 0, 16, 1, 4)
        elif coffee_type == '2':
            self.ingredient(350, 75, 20, 1, 7)
        elif coffee_type == '3':
            self.ingredient(200, 100, 12, 1, 6)

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_add = int(input())
        print('Write how many ml of milk do you want to add:')
        milk_add = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        beans_add = int(input())
        print('Write how many ml of water do you want to add:')
        cups_add = int(input())
        self.ingredient(-water_add, -milk_add, -beans_add, -cups_add, 0)

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


coffee = CoffeeMachine(400, 540, 120, 10, 550)
coffee.action()

