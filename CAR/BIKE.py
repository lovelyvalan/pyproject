from CAR.AUTOMOBILE import Automobile

class Bike(Automobile):
    type = 'yamaha' # class attribute
    def __int__(self,make,model,regno):
        super().__init__(make,model,regno)