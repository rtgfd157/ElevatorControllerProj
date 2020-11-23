class Elevator:
    """
    class that will manage Elevator.
    will move the elevator in the building.
    will get new requests from the controller.
    the class will have sub class of elevator buttons(within).
    """

    def __init__(self, in_currentFloor, in_number_of_floors):
        self.elQueue = []  # 2 values  on each cell - [  isInsidePress=bolean , floornumber ]
        self.direction = 'not_moving' # options "up", "down", "not_moving"
        self.currentFloor = in_currentFloor # program start from in_currentFloor floor
        self.elButtons =  ElevatorButtons(in_number_of_floors) # entity of elevator buttons
        
    def insert_elevator_floor(self, floor_number):
        """
            happens after push of person from inside the elevator
        """

        self.elQueue.insert(0 ,[True, floor_number]) # apepend in start of list
        self.arrange_queue()

        self.set_el_direction() # set the direction of the elevator after inside push
        self.elButtons.floor_inside_butt_pushed(floor_number)  # change light in elevator button

    def set_el_direction(self):
        """
            setting direction of elevator
        """
        #print("setting direction- self.currentFloor : {}  , self.elQueue[0][1] : {} ".format(self.currentFloor, self.elQueue[0][1]))

        if self.currentFloor > self.elQueue[0][1] :
            self.direction = 'down'
        elif self.currentFloor < self.elQueue[0][1] :
            self.direction = 'up'
        else:
            self.direction = 'not_moving'

        #print("self.direction - ",self.direction)

    def call_elevator_from_floor(self,floor_number):
        self.elQueue.append([floor_number, False]) # append in end of list
                
        self.arrange_queue()


    def arrange_queue(self):
        """
            sort elevator floor queue
            sort by two fields first true/false if from inside press, seconed by floor
        """
        if len(self.elQueue)> 0:
            #print(" self.elQueue : ",self.elQueue)
            if self.direction == 'down':
                self.elQueue = sorted(self.elQueue, key=lambda x: (-self.elQueue[0][0], self.elQueue[0][1]))
            else:
                self.elQueue = sorted(self.elQueue, key=lambda x: (self.elQueue[0][0], self.elQueue[0][1]))
                
    def moveElevatorNext(self,):
        if(len(self.elQueue) <1  ):
            self.direction = "not_moving"
        else:
            self.set_el_direction()

        #print("elqueue : ",self.elQueue)
        next_floor =self.elQueue[0]

        self.currentFloor = next_floor[1]
        self.elQueue.pop(0)

        #print("self.direction : #",self.direction,'#')

        if(self.direction == 'up'):
            print("\n    moving up          ")
            print("   ^^^^^^^^^^^^       ")
            print("   ^^^^^^^^^^^^       ")
            print("    moving up          ")
        elif (self.direction == 'down'):
            print("\n   moving  down       ")
            print("   vvvvvvvvvvvv       ")
            print("   vvvvvvvvvvvv       ")
            print("   moving  down       ")

        if(len(self.elQueue) <1  ):
            self.direction = "not_moving"
        else:
            self.set_el_direction()
        
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("elevator stop at {} floor".format(next_floor[1]))
        print("elevator Queue:  {}   way up/down : {}".format(self.elQueue,self.direction))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")

        

                         
class ElevatorButtons:
    """
    class  that will manage the buttons inside the elevator
    mFloorsButtons - array of all the elavtor floors number.array will be in shape of {<floor_number>,<true/false>}.
    isStopButtonPushed - button for managing press of stop(open elevator) in next floor.
    """

    def __init__(self, in_number_of_floors):
        # array of all the elavtor floors number
        self.mFloorsButtons = []
        for i in range(in_number_of_floors):
            self.mFloorsButtons.append({ i : False})
        self.isStopButtonPushed = False

    def floor_inside_butt_pushed(self, floor_number):
        """
            make button light on after push
        """

        for key in self.mFloorsButtons:
            if key == floor_number :
                self.mFloorsButtons[key] = {key: True}

    def floor_inside_butt_off(self, floor_number):
        """
            make button light off after getting to destination
        """

        for key in self.mFloorsButtons:
            if key == floor_number :
                self.mFloorsButtons[key] = {key: False}
