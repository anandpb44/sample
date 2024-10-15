from relo import *
from admin import *
from user import *
while True:
      print('''
          1.Register
          2.Login
          3.Exit''')
      ch=int(input('enter choice:'))
      if ch==1:
         reg()
     
      elif ch==2:
            f,users=log()
            if f==1:
                  while True:
                        print('''
                      1.ADD book
                      2.update
                      3.delete
                      4.view book
                      5.view user
                      6.exit''')
                        ch1=int(input('enter choice:'))
                        if ch1==1:
                              add_book()
                        elif ch1==2:
                              update()
                        elif ch1==3:
                              delete()
                        elif ch1==4:
                              view_book()
                        elif ch1==5:
                              view_user()
                        elif ch1==6:
                              break
                        else:
                              print('Invalid choice !!!')
            elif f==2:
                  while True:
                        print('''
                          1.view profile
                          2.lend book
                          3.return book
                          4.books in hand
                          5.log out''')
                        ch2=int(input('Enter choice'))
                        if ch2==1:
                              view_book()
                        elif ch2==2:
                              lend_book(users)
                        elif ch2==3:
                              re_book(users)
                        elif ch2==4:
                              book_in(users)
                        elif ch2==5:
                              break
                        else:
                              print('invalid choice!!!')
      elif ch==3:
            break
      else:
            print("invalid choice !!!")
            
