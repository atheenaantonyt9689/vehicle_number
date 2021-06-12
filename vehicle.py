import re
class KeralaVehicle:
    def __init__(self):
        self.vehicle_number=[]
        self.vehicle_type=None

    
    def valid_vehicle_number(self,vehicle_number,vehicle_type):
        self.vehicle_number=vehicle_number
        self.vehicle_type=vehicle_type
        regex=(("^KL[0-7][1-3]{2}")+"|([A-Z]{2}[0-9]{4}$)")       
    
        p = re.compile(regex)  
        print(self.vehicle_number)   

        if (self.vehicle_number == None):
            return False

        if(re.search(p,self.vehicle_number)):
            return True
        else:
            return False

 
"""vehicle_number ="KL08AB8976"
vehicle_type="diesel"
obj1=KeralaVehicle()
x=obj1.valid_vehicle_number(vehicle_number,vehicle_type)

print(x)"""








