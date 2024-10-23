class bank:
    def banch(self):
        print('Branch')
class loan(bank):
    def loans(self):
        print("Gold loan,Home Loan,etc")
class depo(bank):
    def deposite(self):
        print('deposite')
    def saving(self):
        print('savings')
class gloan(loan):
    def g(self):
        print('Gold Loan')
class hloan(loan):
    def h(self):
        print("Home Loan")
user=gloan()
user.loans()
user.g()