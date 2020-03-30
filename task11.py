# Create class User with proper methods:
    #     get_account_balance(),  change_password()
    #     Create decorator to handle errors, listed below

class User(): 
    def init(self,name): 
        self.name = name
        self.balance=0
        print("Hello Noka!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("You Withdrew:", amount) 
        else: 
            print("Insufficient balance  ") 
  
    def get_account_balance(self): 
        print("Your Available Balance=",self.balance) 
    
    def change_password(self):
        self.password = []
        self.password = float(input("Enter new password: "))
        print("\n Your password been changed ") 
 
s = User("Noka")   
s.deposit() 
s.withdraw() 
s.get_account_balance()
s.change_password()


# def excep(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except TypeError as e:
#             print('!!!ошибся!!! ', e)
#         except TypeError as e:
#             print('!!!ошибся!!! ', e)
#     return wrapper

# class User:
#     @excep
#     def get_account_balance(self, username):
#         print("Hello "+ username)
#     @excep
#     def change_password(self, password):
#         print(password)

# u = User()
# u.get_account_balance("Wer")
# u.change_password(3453543)