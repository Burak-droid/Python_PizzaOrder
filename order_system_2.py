import csv
from datetime import datetime

# code


class Pizza:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_cost(self):
        raise NotImplementedError("Subclasses must implement get_cost()")




class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza")

    def get_cost(self):
        return 5.45


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita pizza")

    def get_cost(self):
        return 7.56


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza")

    def get_cost(self):
        return 14.85


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza")

    def get_cost(self):
        return 15.78


class Decorator(Pizza):

    def __init__(self, description):
        self.description = description

    def get_description(self):
        return Pizza.get_description(self)

    def get_cost(self):
        return Pizza.get_cost(self)


class Olives(Decorator):
    def __init__(self):
        super().__init__("Olives")

    def get_cost(self):
        return 11.78


class Mushrooms(Decorator):
    def __init__(self):
        super().__init__("Mushrooms")

    def get_cost(self):
        return 10.78


class GoatCheese(Decorator):
    def __init__(self):
        super().__init__("GoatCheese")

    def get_cost(self):
        return 9.68


class Meats(Decorator):
    def __init__(self):
        super().__init__("Meats")

    def get_cost(self):
        return 7.99


class Onions(Decorator):
    def __init__(self):
        super().__init__("Onions")

    def get_cost(self):
        return 8.45


class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn")

    def get_cost(self):
        return 12.74


def main():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open('Order_Database.csv', 'a', newline='') as fp:
        menu = open('menu.txt', 'r')
        content = menu.read()
        margherita_pizza = MargheritaPizza()
        classic_pizza = ClassicPizza()
        Turk_pizza = TurkPizza()
        Dominos_pizza = DominosPizza()
        olives = Olives()
        mushroom = Mushrooms()
        goatCheese = GoatCheese()
        meat = Meats()
        onions = Onions()
        corn = Corn()
        print(content)
        total_count = 0
        pizza_choice = int(input("Please enter the pizza type:"))

        if pizza_choice == 1:
            print(classic_pizza.get_description())
            total_count += classic_pizza.get_cost()
            print(total_count)
            x = classic_pizza.get_description()
        elif pizza_choice == 2:
            print(margherita_pizza.get_description())
            total_count += margherita_pizza.get_cost()
            print(total_count)
            x = margherita_pizza.get_description()
        elif pizza_choice == 3:
            print(Turk_pizza.get_description())
            total_count += Turk_pizza.get_cost()
            print(total_count)
            x = Turk_pizza.get_description()
        elif pizza_choice == 4:
            print(Dominos_pizza.get_description())
            total_count += Dominos_pizza.get_cost()
            print(total_count)
            x = Dominos_pizza.get_description()

        sauce_choice = int(input("Please enter the sauce"))
        if sauce_choice == 11:
            print(olives.get_description())
            total_count += olives.get_cost()
            print(total_count)
            y = olives.get_description()
        elif sauce_choice == 12:
            print(mushroom.get_description())
            total_count += mushroom.get_cost()
            print(total_count)
            y = mushroom.get_description()
        elif sauce_choice == 13:
            print(goatCheese.get_description())
            total_count += goatCheese.get_cost()
            print(total_count)
            y = goatCheese.get_description()
        elif sauce_choice == 14:
            print(meat.get_description())
            total_count += meat.get_cost()
            print(total_count)
            y = meat.get_description()
        elif sauce_choice == 15:
            print(onions.get_description())
            total_count += onions.get_cost()
            print(total_count)
            y = onions.get_description()
        elif sauce_choice == 16:
            print(corn.get_description())
            total_count += corn.get_cost()
            print(total_count)
            y = corn.get_description()
        Name = input("please enter the name: ")
        Tc_No = int(input("please enter the TC no: "))
        Credit_card_no = int(input("please enter the credit card no: "))
        Credit_card_password = int(
            input("please enter the credit card password: "))
        a = csv.writer(fp, delimiter=',')
        data = [['Name', 'Credit No', 'Credit Card Password', 'Pizza Type', 'Sauce Type', 'Total Cost', 'time'],
                [Name, Credit_card_no, Credit_card_password, x, y, total_count, current_time,
                 ],
                ]
        a.writerows(data)
        fp.close()


if __name__ == "__main__":
    main()
