class Shape(object):
    '''形状'''
    # 都有一个area方法
    # 这里用了属性装饰器
    # 下面继承的子类都overwrite了这个方法
    @property
    def area(self):
        pass
 
         
class Rectangle(Shape):
    '''矩形'''
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
         
    @property
    def area(self):
        return self.width * self.height
         
         
class Square(Rectangle):
    '''正方形'''
    def __init__(self, side=0):
        super().__init__(side, side)
         
         
         
class Ellipse(Shape):
    '''椭圆形'''
    pi = 3.1415926535
    def __init__(self, a=0, b=0):
        super().__init__()
        self.a = a
        self.b = b
         
    @property
    def area(self):
        return self.a * self.b * self.pi
         
         
class Circle(Ellipse):
    '''圆形'''
    def __init__(self, r=0):
        super().__init__(r, r)
         
         
shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)]
 
areas = [x.area for x in shapes]
print('areas: ', areas)
total_area = sum(areas)
print('total_area: ', total_area)
