print("-----------------Welcome To ATM-----------------")
class ATM:
    def __init__(self,):
        self.balance = 0
        self.pin = None
        self.card_no = 0
        self.limit = 0
        self.menu()

    def menu(self):
        while True:
            if self.valid_tries() == True:
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
            else:
                break

    def create_pin(self):
       pin = int(input("Enter your pin: "))
       self.pin = pin
       print("pin created successfully")

    def deposit(self):
        if self.pin_validation() == True:
            amt = int(input("Enter the amount want to deposit: "))
            self.balance += amt
            print("Amount successfuly deposited")
        else:
            pass

    def withdraw(self):
        if self.pin_validation() == True:
            amt = int(input("Enter the amount want to withdraw: "))
            if amt <= self.balance:
                print("Amount withdraw successfully")
                self.balance -= amt
            else:
                print("Wrong amount or Low balance")
        else:
            pass

    def check_balance(self):
        if self.pin_validation() == True:
            print(f"Balance: {self.balance}")
        else:
            pass

    def valid_tries(self):
        if self.limit < 3:
            return True
        else:
            print("Your maximum limit of invalid tries have reached. Try again after two days or confirmation")
            return False
        
    def pin_validation(self):
        if self.pin == None:
            print("Choose 1 to set your pin first then move to next option")
            return False
        temp = int(input("Enter your pin: "))
        if temp == self.pin:
            return True
        else:
            self.limit += 1
            print(f"wrong pin entered. wrong tries {self.limit} total wrong tries are 3")
            return False


          

    

x = ATM()