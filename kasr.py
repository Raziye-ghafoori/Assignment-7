

class kasr ():
    def __init__(self,s=0,m=1):
        self.sorat=s
        self.makhraj=m

    def __add__(self ,other):
        if self.makhraj == other.makhraj:
           return (self.sorat +other.sorat ,self.makhraj)
        else:
            return("I can\'t Add")

    def __sub__(self ,other):
        if self.makhraj == other.makhraj:
           return (self.sorat -other.sorat ,self.makhraj)
        else:
            return ("I can\'t Add")
    
    def __mul__(self , other):
        return(self.sorat * other.sorat ,self.makhraj * other.makhraj)
    
    def __truediv__(self , other):
        return(self.sorat * other.makhraj ,self.makhraj * other.sorat)


k1=kasr(3,5)
k2=kasr(5,8)
k3=kasr(6,5)

print("Add")
print(k1+k2)
print(k1+k3)
print("subtract")
print(k1-k2)
print(k1-k3)
print("multiply")
print(k1*k2)
print("divide")
print(k1/k2)
