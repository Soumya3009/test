
class emp:
    def __init__(self, name, dept):
        self.name=name
        self.dept=dept

    def __eq__(self, other):
        print("Hi")
        if self.dept==other.dept:
            return True
        else:
            return False

e1=emp("soumya", "sales")
e2=emp("mani", "sales")

print(id(e1))
print(id(e2))

if e1==e2:
    print("They are same")

else:
    print("They are different")

