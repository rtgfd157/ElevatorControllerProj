
class FloorsClass():
    """
        class that will manage floors.
        isUp, isDown - buttons outside elevator.
        elevatorCurrentFloor -  floor number the elevator at. 
    """
    def __init__(self, elevatorPlace, in_number_of_floors):

        self.floorsArray = []


        for i in range(in_number_of_floors):

                fl =  self.FloorClass(i)
                self.floorsArray.append(fl)
        self.elevatorCurrentFloor = elevatorPlace

    def printFloorsButtOn(self):
        locals =[]

        for i in self.floorsArray:
            if i.isDown or i.isDown:
                locals.append(i.floorNumber)
        print(" buttton pushed on floor  :",locals)

    def togglePushUp(self,floorNumber):
        """
        togglin between pressing on button outside the floor, and removing button on when in destenation.
        """
        for i in self.floorsArray:
            if i == floorNumber:
                self.floorsArray[i].togglePushUp_floor(floorNumber)


    def togglePushDown(self, floorNumber):
        """
        togglin between pressing on button outside the floor, and removing button on when in destenation.
        """
        for i in self.floorsArray:
            if i == floorNumber:
                self.floorsArray[i].togglePushDown_floor(floorNumber)


    class FloorClass():
        """
            class that will represent floor.
        """

        def __init__(self, floorNumber):
            self.isUp=False
            self.isDown=False
            self.floorNumber = floorNumber

        def togglePushUp_floor(self, floorNumber):
            self.isUp = not  self.isUp

        def togglePushDown_floor(self, floorNumber):
            self.isDown = not  self.isDown

    