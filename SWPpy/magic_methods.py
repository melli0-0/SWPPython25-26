
class Cars:
    def __init__(self, model, ps, cost):
        self.model = model
        self.ps = ps
        self.cost = cost

    def __add__(self, a, b):
        if a.isInstance() and b.isInstance():
            return a.ps + b.ps
        return a+b

    def __sub__(self, a, b):
        if a.isInstance() and b.isInstance():
            return a.ps - b.ps
        return a-b

    def __mul__(self, a, b):
        if a.isInstance() and b.isInstance():
            return a.ps * b.cost
        return a * b

    def __eq__(self, a, b):
        if a.isInstance() and b.isInstance():
            return a.ps == b.ps
        return a == b

    def __lt__(self, a,b):
        if a.isInstance() and b.isInstance():
            return a.cost < b.cost
        return a < b

    def __gt__(self, a,b):
        if a.isInstance() and b.isInstance():
            return a.cost > b.cost
        return a > b

    def __str__(a):
        return f"{a.model}, with {a.ps} ps costs {a.cost}$\n" 


class Main():
    audi = Cars("Audi R8", 220, 44800)
    bmw = Cars("BMW M3", 180, 38520.9)
    dodge = Cars("Dodge Challanger", 420, 65900.49)

    print(audi, bmw, dodge)


    print("Addition: ",audi+bmw)
    print("Multiplication: ", dodge * bmw)
    print("Substraction: ",bmw-dodge)
    print("Greater than: ",dodge > bmw)
    print("Equals: ",audi == bmw)
    print("Test: ", audi+5)
