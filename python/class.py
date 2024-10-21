# class bank:
#     # def create(s):
#     def __init__(s):
#         s.id=int(input('Enter Id:'))
#         s.name=input('Enter Your Name:')
#         s.bal=0
#     def balance(self):
#         print('balance:',self.bal)
#     def deposite(s):
#         depo_amt=int(input('Enter Amount:'))
#         s.bal+=depo_amt

# cus1=bank()
# # cus1.create()
# cus1.deposite()
# cus1.balance()

#argument

# class bank:
#     def __init__(s,id,name,bal):
#         s.id=id
#         s.name=name
#         s.bal=bal
#     def balance(self):
#         print('balance:',self.bal)
#     def deposite(s,amt):
#         s.bal+=amt

# cus1=bank(1,'anand',8889)
# cus1.deposite(8889)
# cus1.balance()


# class syn:
#     def php(self):
#         print('php')
#     def python(self):
#         print('python')

# class nova(syn):
#     def web(self):
#         print('Web')
#     def dm(self):
#         print('dm')
# akhil=syn()
# akhil.php()
# staff1=nova()
# staff1.php()

class bank:
    def gloan(self):
        print('G loan')
    def Hloan(self):
        print('H laon')

class staff(bank):
    def account(self):
        print('account')
    def manager(self):
        print('Manager')
akhil=bank()
akhil.gloan()
staff1=staff()
staff1.manager()