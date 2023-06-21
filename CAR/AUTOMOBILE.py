class Automobile():

    def __init__(self, make, model, regno):
        self._make = make
        self.model = model
        self.regno = regno
        self.batt = 0


    @property
    def make(self):
        return self._make


    @make.getter
    def make(self):
        print(f'returning {self._make}')
        return self._make

    @make.setter
    def make(self, make):
        print(f'setting {self._make} to {make}')
        self._make = make

    @make.deleter
    def make(self):
        print(f'Deleting..{self._make}')
        del self._make