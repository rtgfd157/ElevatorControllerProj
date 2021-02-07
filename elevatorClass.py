import copy
import threading

class Elevators:
    """
        class that will manage all elevators in building

    """
    def __init__(self,in_number_of_floors ,in_number_of_elevators):
        self.lock = threading.Lock()

        self.elvators_arr = []
        for i in range(in_number_of_elevators):
            le = Elevator(in_number_of_floors , i )
            self.elvators_arr.append(le)

    def moveElevatorNext(self,floors_instance):
        for el in self.elvators_arr:
            self.lock.acquire()
            #print( f'el.elQueue : {el.elQueue} el_number: {el.el_number}' )
            el.moveElevatorNext(floors_instance)
            self.lock.release()


    def handler_add_stop_to_elevators_from_floor(self, floor,direction):
        """
            method to choose elevator by same direction and fewer stops in queue line
        """
        print('###########################')
        print(  "inside handler_add_stop_to_elevators_from_floor" )

        self.lock.acquire()
        arr = None
        arr = copy.deepcopy(self.elvators_arr)
        # for el in arr:
        #     print(f'el.el_number {el.el_number}  el.direction{el.direction}')  
        
        if direction <0:
            arr= sorted( arr, key=lambda x: ( x.direction, x.elQueue ))
        else:
            arr= sorted( arr, key=lambda x: ( -x.direction, x.elQueue ))

        el_number = arr[0].el_number # the first elevator that is in best shape
        self.elvators_arr[el_number].elQueue.append(floor)
        self.lock.release()


    def handler_inside_elevator_butt_press(self, elevator_number ,floor):
        if floor not in self.elvators_arr[elevator_number].elQueue:
            self.elvators_arr[elevator_number].elQueue.append(floor)


 

class Elevator:
    """
    class that will manage Elevator.
    will move the elevator in the building.
    will get new requests from the controller.
    the class will have sub class of elevator buttons(within).
    """

    def __init__(self, in_number_of_floors,in_el_number):
        #self.lock = threading.Lock() # make bug need to check
        self.elQueue = [] #[ floornumber]            ///floornumber: number} isInsidePress=bolean 
        self.direction = 0 # options "up" = 1, "down" = -1, "not_moving" = 0
        self.currentFloor = self.init_current_floor() # program start from in_currentFloor floor
        self.elButtons =  ElevatorButtons(in_number_of_floors) # entity of elevator buttons
        self.el_number = in_el_number

    def init_current_floor(self):
        return 0
        #self.currentFloor = 0

    def get_current_floor_and_direction(self):
        return (  self.currentFloor, self.direction )
    
    def check_if_elevator_in_same_direction(self, direction):
        if self.direction == direction:
            return True
        return False

    def insert_elevator_floor(self, floor_number):
        """
            happens after push of person from inside the elevator
        """
        self.elQueue.append(floor_number) # apepend in start of list
        
        self.set_el_direction() # set the direction of the elevator after inside push
        self.elButtons.floor_inside_butt_pushed(floor_number)  # change light in elevator button
        self.set_el_direction()

    def set_el_direction(self):
        """
            setting direction of elevator
        """
        #print(f'self.elQueue {self.elQueue}, self.currentFloor {self.currentFloor}  ')
        #print("setting direction- self.currentFloor : {}  , self.elQueue[0][1] : {} ".format(self.currentFloor, self.elQueue[0][1]))
        if self.elQueue.count == 0:
            self.direction = 0
        elif self.currentFloor > self.elQueue[0] :
            self.direction = -1
        elif self.currentFloor < self.elQueue[0] :
            self.direction = 1
        else:
            self.direction = 0



    def arrange_queue(self):
        """
            sort elevator floor queue
            sort by two fields first true/false if from inside press, seconed by floor
        """
        #print(f'el queue: {self.elQueue} from arrange queue')
        if len(self.elQueue)> 0:
            #print(" self.elQueue : ",self.elQueue)
            if self.direction == -1 :
                self.elQueue.sort(reverse = True)
                #self.elQueue = sorted(self.elQueue, key=lambda x: (-self.elQueue))
            else:
                self.elQueue.sort()
                #self.elQueue = sorted(self.elQueue, key=lambda x: (self.elQueue))
                
    def moveElevatorNext(self,floors_instance):
        lock = threading.Lock()
        lock.acquire(0)
        if(len(self.elQueue) <1  ):
            self.direction = 0
            return
        else:
            self.set_el_direction()
            self.arrange_queue()

        next_floor =self.elQueue[0]

        self.currentFloor = next_floor
        self.elQueue.pop(0)

        # floor button off after getting to  destenation
        self.elButtons.floor_inside_butt_off(self.currentFloor)

        floors_instance.floor_turn_on_PushDown(self.currentFloor)
        if(self.direction == 1):
            print("\n    moving up          ")
            print("   ^^^^^^^^^^^^       ")
            print("   ^^^^^^^^^^^^       ")
            print("    moving up          ")
        elif (self.direction == -1):
            print("\n   moving  down       ")
            print("   vvvvvvvvvvvv       ")
            print("   vvvvvvvvvvvv       ")
            print("   moving  down       ")

        if(len(self.elQueue) <1  ):
            self.direction = 0
        else:
            self.set_el_direction()
        
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("elevator number:{} stop at {} floor".format(self.el_number,next_floor))
        print("elevator Queue:  {}   way (1)up/down(-1) : {}".format(self.elQueue,self.direction))
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
        lock.release()
        

        

                         
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
