class Mother:
    def house(self):
        return f"House Built Newly"

class Daughter(Mother):
    def factory(self):
        return f"1000 workers working in the factory"

d1=Daughter()
print(d1.house())
print(d1.factory())