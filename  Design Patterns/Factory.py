class ShapeInterface:
    def draw(self): pass
    
class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")
        
class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")
        
class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type =='circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, 'Couldn\'t find shape' + type

f = ShapeFactory()
c = f.getShape('circle')
s = f.getShape('square')
print(f)
print(s)
print(c)
Square.draw 
