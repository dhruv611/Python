class a:
    x=0
    name=None
    def __init__(self,name1):   #Constructor
        self.name = name1     #instialising value in class variable name
        print('Constructor called for ',self.name)
    def a1(self):             # method a1 of class a
        self.x=self.x+1
        print('x: ',self.x)

class b(a):                    #class b extends a means b is inheriting a; now object of b can call a1
    y=0
    def b1(self):
        self.y=self.y+2
        self.a1()
        print(self.y)
