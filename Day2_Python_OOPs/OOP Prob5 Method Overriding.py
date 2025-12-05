class Father:
    def house(self,colour="Blue"):
        self.colour=colour

class son(Father):
    def house(self,colour):
        self.colour=colour
        return self.colour

obj1=son()
print(obj1.house("White"))