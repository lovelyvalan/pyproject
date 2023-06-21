class Parent():
    def __init__(self,dname,mname,year):
        self.dname=dname
        self.mname=mname
        self.bdyear=year

    def calling(self):
        print(f'my father {self.dname} and my mother name is {self.mname} by {self.bdyear}')

    def child(self,c1,c2):
        print(f'{c1} , {c2}')

    def yr(self):
        print(self.bdyear)

p=Parent('jesudass','lucia',year=1965)
p.calling()
p.child('dam','sweetha')
p.yr=2045
print(p.yr)
print('============================')
class Child(Parent):
    def __int__(self,fname,mname):
        Parent.__init__(self,fname,mname,year=0)

c = Child('dass','lucia',1965)
c.calling()
c.child('valan','christi')
c.year=2023
print(c.year)
