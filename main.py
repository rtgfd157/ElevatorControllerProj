import time
import asyncio
import random

from elevatorClass import Elevator
from floorsClass import FloorsClass


class ElevatorController:
    """
    controller
    """

    def __init__(self, in_currentFloor, in_number_of_floors):

        self.numberOfFloors = in_number_of_floors

        self.elevator_instance = Elevator(in_currentFloor, in_number_of_floors)
        elevatorPlace = self.elevator_instance.currentFloor  # elevator current place
        self.floors_instance = FloorsClass(elevatorPlace, in_number_of_floors)

    async def startprogram(self):
        exit = False
        i = 0

        while exit == False and i < 30   :

            # need to be thread
            self.randomlyGetFloorInputs()

            speed_of_elevator = random.randint(1, 4)
            if speed_of_elevator % 2 == 0:

                if len(self.elevator_instance.elQueue) > 0 :

                    #print("self.elevator_instance.elQueue: ",len(self.elevator_instance.elQueue))
                    self.elevator_instance.moveElevatorNext()
                    self.updateButttonFloorAfterArriving()
                    

                    # need to be thread
                    self.randomlyGetElevatorButtInputs(self.elevator_instance.currentFloor) # pushing button from inside the elevator

                    

            # print("Hello World")
            time.sleep(4)
            i += 1

    def randomlyGetFloorInputs(self):
        r = random.randint(0, 10)

        if r % 4 == 0:

            # make press on floor
            if r % 8 == 0:
                r2 = random.randint(
                    1, self.numberOfFloors - 1
                )  # random  floor picking ,  0 floor cant be down
                self.floors_instance.floorsArray[r2].isDown = True
                
                print("@@@@@@@ \ncurrent press from {} floor  way Down".format(r2))
                print("elevator at floor: {} ".format(self.elevator_instance.currentFloor))
                self.floors_instance.printFloorsButtOn()
                print("@@@@@@@ ")
                #print("before : ",self.elevator_instance.elQueue)
                self.elevator_instance.insert_elevator_floor(r2)
                #print("after : ",self.elevator_instance.elQueue)
            else:
                r2 = random.randint(1, self.numberOfFloors - 2)  # random  floor picking ,  last floor cant be up
                self.floors_instance.floorsArray[r2].isUp = True
                #print("before : ",self.elevator_instance.elQueue)
                self.elevator_instance.insert_elevator_floor(r2)
                #print("after : ",self.elevator_instance.elQueue)
                print("@@@@@@@ \ncurrent press from {} floor  way Down".format(r2))
                print("elevator at floor: {} ".format(self.elevator_instance.currentFloor))
                self.floors_instance.printFloorsButtOn()
                print("@@@@@@@ ")


    def randomlyGetElevatorButtInputs(self, currentFloor):

        # print("randomlyGetElevatorButtInputs")
        # print("current_floor : ",current_floor)
        # print("elf.floors_instance.floorsArray[currentFloor].isDown :",self.floors_instance.floorsArray[currentFloor].isDown)
        # print("self.floors_instance.floorsArray[currentFloor].isUp :",self.floors_instance.floorsArray[currentFloor].isUp)

        if self.floors_instance.floorsArray[currentFloor].isDown:
            r = random.randint(0, currentFloor)
            self.elevator_instance.insert_elevator_floor(r)
            print("&&&&&&&&&&&&")
            print("press from elevator on floor {}  on floor {} button".format(current_floor, r))
            print("&&&&&&&&&&&&")
            
        elif self.floors_instance.floorsArray[currentFloor].isUp:
            r = random.randint(currentFloor, self.numberOfFloors - 1)
            print("&&&&&&&&&&&&")
            print("press from elevator on floor {}  on floor {} button".format(current_floor, r))            
            print("&&&&&&&&&&&&")

    def updateButttonFloorAfterArriving(self):
        """
            updating floor button after arriving
        """
        if self.floors_instance.floorsArray[self.elevator_instance.currentFloor].isUp:
            self.floors_instance.floorsArray[self.elevator_instance.currentFloor].isUp = False  
        elif self.floors_instance.floorsArray[self.elevator_instance.currentFloor].isDown:
            self.floors_instance.floorsArray[self.elevator_instance.currentFloor].isDown =False


if __name__ == "__main__":
    current_floor = 0
    number_of_floors = M = 5
    ec = ElevatorController(current_floor, number_of_floors)
    asyncio.run(ec.startprogram())
