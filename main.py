import time
import asyncio
import random

from elevatorClass import Elevator
from floorsClass import FloorsClass

class ElevatorController:
    """
        controller
    """
    def __init__(self,in_currentFloor, in_number_of_floors):

        self.numberOfFloors = in_number_of_floors

        self.elevator_instance =  Elevator(in_currentFloor, in_number_of_floors) 
        elevatorPlace = self.elevator_instance.currentFloor # elevator current place
        self.floors_instance = FloorsClass(elevatorPlace , in_number_of_floors)  

    async  def startprogram(self):
        exit = False
        i=0

        while( exit == False and i< 20 ):
            self.randomlyGetFloorInputs()

            if self.elevator_instance.elQueue >0:
                self.elevator_instance.moveElevatorNext()

                current_floor = self.elevator_instance.currentFloor

                if self.floors_instance.floorsArray[current_floor].isUp or self.floors_instance.floorsArray[current_floor].isUp:
                     self.randomlyGetElevatorButtInputs(current_floor)

            #print("Hello World")
            time.sleep(2) 

    def randomlyGetFloorInputs(self):
        r = random.randint(0,10)

        if r % 4 == 0:

            # make press on floor
            if r % 8 == 0:
                r2 =random.randint(1,self.numberOfFloors-1) # random  floor picking ,  0 floor cant be down
                self.floors_instance.floorsArray[r2].isDown =True
                print("@@@@@@@ \n  current press from {} floor  way Down \n@@@@@@@ \n".format(r2))
            else:
                r2 =random.randint(1,self.numberOfFloors-2) # random  floor picking ,  last floor cant be up
                self.floors_instance.floorsArray[r2].isUp =True
                print("@@@@@@@ \n press from {} floor  way Up \n@@@@@@@ \n".format(r2))

    def randomlyGetElevatorButtInputs(self, currentFloor):
        
        if self.floors_instance.floorsArray[currentFloor].isDown:
            r = random.randint(0,currentFloor)
            self.elevator_instance.insert_elevator_floor(r)
            print("&&&&&&&&&&&&\nn  press from elevator on floor {}  on floor {} button &&&&&&&&&&&&\nn".format(current_floor,r))
        elif  self.floors_instance.floorsArray[currentFloor].isUp: 
            r = random.randint(currentFloor, self.numberOfFloors-1)
            self.elevator_instance.insert_elevator_floor(r)
            print("&&&&&&&&&&&&\nn  press from elevator on floor {}  on floor {} button &&&&&&&&&&&&\nn".format(current_floor,r))


if __name__ == "__main__":
    current_floor = 0
    number_of_floors = M = 5
    ec =  ElevatorController(current_floor, number_of_floors)  
    asyncio.run(ec.startprogram())
    
