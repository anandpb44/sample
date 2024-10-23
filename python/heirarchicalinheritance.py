class shop:
    def smart_pho(self):
        print('Smart phones')
    def head_pho(self):
        print('Head Phones')
class staff(shop):
    def cus_service(self):
        print("custamer Service")
class user(shop):
    def reg (self):
        print('Register')
    def online_pay(self):
        print('online Payment')
    def cash(self):
        print('Cash')
us=user()
us.smart_pho()
sta=staff()
sta.cus_service()