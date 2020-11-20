
class FloorsClass():
    """
        class that will manage floor.
        isUp, isDown - buttons outside elevator.
        elevatorCurrentFloor -  floor number the elevator at. 
    """
    def __init__(self, elevatorPlace, in_number_of_floors):

        self.floorsArray = []

        for i in range(in_number_of_floors):
                self.floorsArray.append({"floor": i, "isUp": False , "isDown":False})
        self.elevatorCurrentFloor = elevatorPlace

    def togglePushUp(self,floorNumber):
        """
        togglin between pressing on button outside the floor, and removing button on when in destenation.
        """
        self.floorsArray[floorNumber]['isUp'] = not  self.floorsArray[floorNumber]['isUp']

    def togglePushDown(self, floorNumber):
        """
        togglin between pressing on button outside the floor, and removing button on when in destenation.
        """
        self.floorsArray[floorNumber]['isDown'] = not self.floorsArray[floorNumber]['isDown']

    