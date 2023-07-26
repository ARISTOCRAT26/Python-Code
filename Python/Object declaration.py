class Human:
    
    attr1 = "mammal"
    attr2 = "male human"
    attr3 = "female human"
 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Human()

print(Rodger.attr1)
Rodger.fun()