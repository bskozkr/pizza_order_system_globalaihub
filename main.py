import csv
import datetime

# Created a list in order to create the .txt file that exists of pizza and sauce types. Using file operations, we implemented the list into .txt file.
pizza_list = ["*Please Choose a Pizza Base:\n", "1: Classic --> €5\n", "2: Margherita --> €4\n",
              "3: Turk Pizza --> €8\n", "4: Plain Pizza --> €3\n", "*and sauce of your choice:\n",
              "11: Olives --> €2\n", "12: Mushrooms --> €1\n", "13: Goat Cheese --> €3\n", "14: Meat --> €4\n",
              "15: Onions --> €1\n", "16: Corns --> €2"]
with open("PizzaMenu.txt", "w") as file1:
    for word in pizza_list:
        file1.write(word)
        file1.write("\n")


# Created the pizza class, this class is the base for all the operations happening in the system.
class Pizza:

    def get_cost(self):  # Method that takes the cost of pizzas and sauces.
        return self.cost

    def get_description(self):  # Method that takes the descriptions of pizzas and sauces.
        return self.description


# These separate classes have the cost and description knowledge of each pizza type.
class Classic(Pizza):
    description = "Classic pizza have tomato sauce, cheese, mushrooms and salami in our restaurant.\n"
    cost = 5


class Turk(Pizza):
    description = "Turk pizza have tomato sauce, cheese and meat in our restaurant.\n"
    cost = 8


class Margherita(Pizza):
    description = "Margherita pizza have tomato sauce, cheese and basil in our restaurant.\n"
    cost = 4


class Plain(Pizza):
    description = "Plain pizza have tomato sauce and cheese in our restaurant.\n"
    cost = 3


# Decorator class uses the knowledge in separate pizza and sauce classes and calculates the total cost for pizza and
# total description that consists of pizza and sauce. @staticmethod is used because methods inside of decorator class
# does not make changeable operations, they just directly calculates the cost and description.


class Decorator:

    @staticmethod
    def get_cost(cost_of_pizza, cost_of_sauce):
        total = cost_of_sauce + cost_of_pizza
        return total

    @staticmethod
    def get_description(description_of_pizza, description_of_sauce):
        total = description_of_pizza + description_of_sauce
        return total


# These separate classes have the cost and description knowledge of each sauce type.


class Olives(Decorator):
    cost = 2
    description = "You have chosen olives. Olive has tangy flavour with bitter and salty at the same time, delicious " \
                  "choice for your pizza."


class Mushrooms(Decorator):
    cost = 1
    description = "You have chosen mushrooms. Mushrooms are one of the main ingredient for mixed pizza. "


class GoatCheese(Decorator):
    cost = 3
    description = "You have chosen goat cheese. Goat cheese is an indispensable ingredient of pizza, such a good " \
                  "choice of sauce for cheese lovers."


class Meat(Decorator):
    cost = 4
    description = "You have chosen meat. For non-vegans, non-vegetarians and those who hate veggies since childhood :)."


class Onions(Decorator):
    cost = 1
    description = "You have chosen onions. Not for everyone but such a delicious taste, specially with meat."


class Corns(Decorator):
    cost = 2
    description = "You have chosen corns. Everybody loves, always all the time chosen for any kind of pizza."


########################################################################################################################

# main() function actualizes the file operations to read the menu, takes input of sauces and pizza, determines the
# information of pizza and sauce to print and takes the payment information from user. Creates a .csv file and
# transfers these information to the csv file.


def main():
    f = open('PizzaMenu.txt', 'r')  # Reading .txt file and print it on the console to make the user choose.
    menu = f.read()

    print(menu)

    f.close()

    while 1:

        pizza_in = int(input("Please enter the number of pizza of choice: "))
        sauce_in = int(input("Please enter the number of sauce of choice: "))

        if pizza_in == 1:  # Here checking the condition for all the input with given numbers.
            choice_of_pizza = Classic()
        elif pizza_in == 2:
            choice_of_pizza = Margherita()
        elif pizza_in == 3:
            choice_of_pizza = Turk()
        elif pizza_in == 4:
            choice_of_pizza = Plain()

        if sauce_in == 11:
            choice_of_sauce = Olives()
        elif sauce_in == 12:
            choice_of_sauce = Mushrooms()
        elif sauce_in == 13:
            choice_of_sauce = GoatCheese()
        elif sauce_in == 14:
            choice_of_sauce = Meat()
        elif sauce_in == 15:
            choice_of_sauce = Onions()
        elif sauce_in == 16:
            choice_of_sauce = Corns()

        try:
            gesamtmenge = Decorator.get_cost(choice_of_pizza.cost,
                                             choice_of_sauce.cost)  # Using decorator class to give the total cost and description.
            gesamtbeschreibung = Decorator.get_description(choice_of_pizza.description, choice_of_sauce.description)
            print("Total cost of pizza with sauces: €" + str(gesamtmenge))
            print("You can see the description of each ingredient and pizza: " + gesamtbeschreibung)
            break

        except:
            print(
                "The number you have given is not on our scope.")  # If there is a mistake prints this to inform the user.
            continue

    now = datetime.datetime.now()  # Date and time.
    date_and_time = now.strftime("%H:%M:%S")  # Simplifies the time.

    # Take the information as input from user.
    name_of_user = input("Please enter your name: ")
    id_of_user = input("Please enter your User ID: ")
    creditcard_number = input("Please enter your credit card number: ")
    creditcard_password = input("Please enter your credit card password: ")

    data_list = [name_of_user, id_of_user, creditcard_number, creditcard_password,
                 date_and_time]  # Make a list using these datas.

    with open('UserData.csv', 'w') as data_file:  # Open a csv file and transfer the input data to this file.

        writer = csv.writer(data_file, delimiter='\n')

        writer.writerow(data_list)


main()
