
from elevatorClass import Elevator

class ElevatorController:
    def __init__(self,in_currentFloor, in_number_of_floors):

        elevator_instance =  Elevator(in_currentFloor, in_number_of_floors) 



    def startprogram(self):
        print("Hello World") ;

if __name__ == "__main__":
    current_floor = 0
    number_of_floors = 5
    ec =  ElevatorController(current_floor, number_of_floors)  
    ec.startprogram()
