from abc import ABC,abstractmethod
class clg():
    @abstractmethod
    def register(self):
        print('Register')
    def class_room(self):
        print("Class room")
    def ground(self):
        print("Ground")
class std(clg):
    def register(self):
        name=input('name:')
        email=input('email:')
        phno=input('phno:')
    def note(self):
        print('College Notes')
class staff(clg):
    def register(self):
        name=input('name:')
        exp=input('Experience:')
        sub=input('sub:')
    def exam_pappers(self):
        print("Exam Pappers")

std1=std()
std1.register()
s=staff()
s.register()