
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = "("+str(self.x)+", "+str(self.y)+")"
        return s

p = Point(2,3)
print(p)