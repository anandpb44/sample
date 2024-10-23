class bank:
    def __init__(self):
        print('''
            SBI
            Branch:chalissery
            ifc:SBI100567
            location:pattambi road chalissery
            
                ''')
    def deposite(self):
        print("Amount deposited")
class user(bank):
    def __init__(self):
        #To slove overwritting use super() 
        super().__init__()
        self.name=input("Enter Your name:")
        self.email=input("Enter Email Address:")
        self.pho=int(input("Enter Phoine Number:"))
anand=user()