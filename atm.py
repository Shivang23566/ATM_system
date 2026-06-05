print("-----------------Welcome To ATM-----------------")

# the progress has made
# now the remaining logic is to set three tries at the pin check upon wrong entry 
# and the pin verify logic if the pin is even set already or still none


class ATM:
    def __init__(self,):
        self.balance = 0
        self.pin = None
        self.card_no = 0
        self.menu()

    def menu(self):
        while True:
            print("""How would you like to proceed ?  
                           1. Enter 1 to create pin.
                           2. Enter 2 to deposit.
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance.
                           5. Enter 5 to exit.""")
            num = int(input("Enter your input: "))
            if num == 1:
                self.create_pin()
            elif num == 2:
                self.deposit()
            elif num == 3:
                self.withdraw()
            elif num == 4:
                self.check_balance()
            elif num == 5:
                print("See you later")
                break
            else:
                print("Enter a valid choice")
        

    def create_pin(self):
       pin = int(input("Enter your pin: "))
       self.pin = pin
       print("pin created successfully")

    def deposit(self):
        if self.pin != None:
            temp = int(input("Enter you pin: "))
            if temp == self.pin:
                amt = int(input("Enter the amount want to deposit: "))
                self.balance += amt
                print("Amount successfuly deposited")
            else:
                print("Envalid pin !")
        else:
            print("Set your pin first")

    def withdraw(self):
        if self.pin != None:
            temp = int(input("Enter your pin: "))
            if temp == self.pin:
                amt = int(input("Enter the amount want to withdraw: "))
                if amt <= self.balance:
                    print("Amount withdraw successfully")
                    self.balance -= amt
                else:
                    print("Wrong amount or Low balance")
            else:
                print("Envalid pin")
        else:
            print("Set your pin first")

    def check_balance(self):
        if self.pin != None:
            temp = int(input("Enter your pin: "))
            if self.pin == temp:
                print(f"Balance: {self.balance}")
            else:
                print("Invalid pin")
        else:
            print("Set your pin first")

          

    

x = ATM()
# x = input("Enter your balance")
# y = input("Enter your Pin")

# z = ATM(x,y)
# print(z.balance,z.pin)
