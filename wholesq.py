#!/usr/bin/env python3

class express:
    def getvalue(self):
        self.a=int(input("Enter a: "))
        self.b=int(input("Enter b: "))
    def find(self):
        self.ans=(self.a**2)+(self.b**2)+(2*self.a*self.b)

    def show(self):
        print("The result is: ",self.ans)

obj=express()
obj.getvalue()
obj.find()
obj.show()


