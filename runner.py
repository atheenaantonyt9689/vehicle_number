import csv
from vehicle import KeralaVehicle
def runner():

    with open('vehicle_list.csv','r') as file:
        reader =csv.reader(file) 
        vehicle_list=[] 
        vehicle_type=[] 
        for i in reader:
            V=i[0]
            #print(type(V))
            v_type=i[2]

            vehicle_list.append(V)
            vehicle_type.append(v_type)    

    #vehicle_number =["KL08AB8976","kloooojju"]
    #vehicle_type="diesel"
    obj1=KeralaVehicle()
    x=obj1.valid_vehicle_number(vehicle_list,vehicle_type)
    print(" valid state: ",x)
    

runner()
