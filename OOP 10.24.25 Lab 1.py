class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_num = ""
        self.cname = ""
        self.phone = ""
        self.email = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []

    def create_customer(self):
        self.cid = input("Enter customer ID: ")
        self.acc_num = input("Enter account number: ")
        self.cname = input("Enter customer name: ")
        self.phone = input("Enter phone on file: ")
        self.email = input("Enter customer email: ")
        self.balance = float(input("Enter current account balance: "))

    def debit_from(self):
        self.cid = input("Enter customer ID: ")
        self.balance = self.balance - int(input("Enter amount to debit: "))

    def credit_to(self):
        self.cid = input("Enter customer ID: ")
        self.balance = self.balance + int(input("Enter amount to credit: "))

    def assign_credit_card(self, card):
        self.credit_card.append(card)

    def assign_debit_card(self, card):
        self.debit_card.append(card)

    def display_all(self):
        print("Customer ID: ", self.cid)
        print("Account Number: ", self.acc_num)
        print("Customer Name: ", self.cname)
        print("Phone Number: ", self.phone)
        print("Email: ", self.email)
        print("Account Balance: ", self.balance)
        for x in self.credit_card:
            print("Credit Cards: ", x.card_num)
        for x in self.debit_card:
            print("Debit Card: ", x.card_num)



class Card:
    def __init__(self):
        self.type = ""
        self.card_num = ""
        self.cvv = ""
        self.expire_date = ""
        self.balance = 00.

    def create_card(self):
        self.type = input("Enter card type: ")
        self.card_num = input("Enter card number: ")
        self.cvv = input("Enter CVV: ")
        self.expire_date = input("Enter expiration date: ")
        self.balance = float(input("Enter card balance: "))

    def display_card(self):
        print("Card Type: ", self.type)
        print("Card Number: ", self.card_num)
        print("CVV: ", self.cvv)
        print("Expiration Date: ", self.expire_date)
        print("Balance: ", self.balance)



import pickle

while True:
    print("----- Main Code: Menu -----")
    print("1. Create a customer ")
    print("2. Create a card ")
    print("3. Transfer funds between customers ")
    print("4. Assign a card ")
    print("5. Display customer details ")
    print("6. Display card details ")
    print("7. Add information to file ")
    print("8. Print file information ")
    print("9. Quit ")
    option = input("Select a function: ")

    if option == "1":
        new_customer = Customer()
        new_customer.create_customer()

    elif option == "2":
        new_card = Card()
        new_card.create_card()

    elif option == "3":
        while True:
            print("1. Debit from customer ")
            print("2. Credit to customer ")
            print("3. Return to main menu ")
            option = input("Select a function: ")
            if option == "1":
                new_customer.debit_from()
            elif option == "2":
                new_customer.credit_to()
            elif option == "3":
                break

    elif option == "4":
        while True:
            print("1. Assign credit card ")
            print("2. Assign debit card ")
            print("3. Return to main menu ")
            option = input("Select a function: ")
            if option == "1":
                new_customer.assign_credit_card(new_card)
            elif option == "2":
                new_customer.assign_debit_card(new_card)
            elif option == "3":
                break

    elif option == "5":
        new_customer.display_all()

    elif option == "6":
        new_card.display_card()

    elif option == "7":
        f1 = open("customers.dat", "ab")
        pickle.dump(new_customer, f1)
        f1.close()

        print("Saved! ")

    elif option == "8":
        f2 = open("customers.dat", "rb")
        while True:
            try:
                data = pickle.load(f2)
                data.display_all()
            except EOFError:
                break

    elif option == "9":
        break