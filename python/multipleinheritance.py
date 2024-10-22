# class school:
#     def class_room(self):
#         print('Class room')
#     def exam(self):
#         print('Exam')
# class tution:
#     def note(self):
#         print("note")
# class student(school,tution):
#     def uniform(self):
#         print('Uniform')
# std=student()
# std.class_room()
# std.exam()
class library:
    def books(self):
        print('Books ')
class user:
    def details(self):
        print('user details')
class admin(library,user):
    def data(self):
        print('Details of user,books')
adm=admin()
adm.books()