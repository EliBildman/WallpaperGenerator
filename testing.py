class C1(object):
    def __init__(self, x):
        self.x = x

    def print_thing(self):
        print self.x

class C2(C1):

    def __init__(self):
        C1.__init__(self, 20)


y = C2()
y.print_thing()
