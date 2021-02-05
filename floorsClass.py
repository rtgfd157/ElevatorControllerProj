class FloorsClass():
    """
        class that will manage floors.
        isUp, isDown - buttons outside elevator.
    """
    def __init__(self, in_number_of_floors):

        self.floorsArray = []
        for i in range(in_number_of_floors):

                fl =  FloorClass(i)
                self.floorsArray.append(fl)

    def printFloorsButtOn(self):
        """
            printing floor buttons that are pressed and there direction
        """
        locals =[]

        for i in self.floorsArray:
            if i.isDown: locals.append( ( 'down: '+ i.floorNumber )  ) 
            elif i.isUp: locals.append( ( 'up: '+ i.floorNumber )  )
                
        print("buttton's array pushed on floors  :\n",locals)

    def floor_turn_on_PushDown(self, floorNumber):
        """
            pressing on button outside the floor.
        """
        print(f'press down on {floorNumber} floor ')
        self.floorsArray[floorNumber].isDown = True 

    def floor_turn_off_PushDown(self, floorNumber):
        """
            pressing on button outside the floor.
        """
        self.floorsArray[floorNumber].isDown = False

    def floor_turn_on_PushUp(self, floorNumber):
        """
            pressing on button outside the floor.
        """
        print(f'press up on {floorNumber} floor ')
        self.floorsArray[floorNumber].isUp = True 

    def floor_turn_off_PushUp(self, floorNumber):
        """
            pressing on button outside the floor.
        """
        self.floorsArray[floorNumber].isU = False



class FloorClass():
    """
        class that will represent floor Button(outside elevator).
    """

    def __init__(self, floorNumber):
        self.isUp=False
        self.isDown=False
        self.floorNumber = floorNumber        

    