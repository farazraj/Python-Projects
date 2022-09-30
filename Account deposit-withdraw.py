class Account():

        
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    #to convert the object to string for the printing
    def __str__(self):
        return f'Account owner: {self.owner} \nBalance: {self.balance}'
    
    #payment deposition
    def deposit(self,amount):

        self.balance = self.balance + amount
        print(f"The amount of {amount} has been deposited in the account of {self.owner} ")
        
    #payment withdrawal with condition if fund not available
    def withdraw(self, amount):
        
        
            if amount < self.balance:
                self.balance = self.balance - amount
                print(f"The amount of {amount} has been withdrawn from the acount of {self.owner}")
                
            else:
                return 'Funds Unavailable'
            

#creating instance of the class
acc = Account('Faraz', 500)

# printing the object
print(acc)

#to deposit the amount
acc.deposit(100)

#to withdraw the amount
acc.withdraw(50)

#to exceed the withdrawn amount than balance
acc.withdraw(1000)

#show balance again
print(acc)


