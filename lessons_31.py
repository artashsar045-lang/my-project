"""1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։"""
from jsonschema.validators import extend


class MyList:
    def __init__(self,*args):
        self.l = list(args)

    def append(self, value):
        return self.l.append(value)

    def remove(self, value):
        return self.l.remove(value)

    def len(self):
        return len(self.l)

    def sorted(self):
        return sorted(self.l)

    def reverse(self):
        reversed(self.l)
        return self.l

    def pop(self):
        return self.l[-1]

    def extend(self,*args,**kwargs):
        return self.l.extend(*args,**kwargs)

    def __str__(self):
        return str(self.l)

l1 = MyList(5,6,4,9)
l1.append(10)
print(l1)
print(l1.len())
print(l1.remove(5))
print(l1.sorted())
print(l1.reverse())
print(l1.pop())
l1.extend("list")
print(l1)

