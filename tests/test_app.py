import unittest
import random
from start_program  import ElevatorController
import floorsClass
from elevatorClass import Elevators, Elevator
#from floorsClass import floor_turn_off_PushUp

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.in_number_of_floors=6
        self.in_number_of_elevators = 5
        self.el_controller = ElevatorController (self.in_number_of_floors,self.in_number_of_elevators)

    def check_number_of_floors(self):
        print( self.el_controller)

    def test_current_floor(self):
        self.assertEqual(self.el_controller.elevators_instance.elvators_arr[0].currentFloor , 0)

    def test_number_of_elevators(self):
        self.assertEqual( len(self.el_controller.elevators_instance.elvators_arr) , self.in_number_of_elevators)
    
    def test_number_of_floors(self):
        self.assertEqual( len(self.el_controller.floors_instance.floorsArray) , self.in_number_of_floors)

    def test_floor_change_on_off(self):

        num = random.randrange(0,self.in_number_of_floors - 1)
        
        floorsClass.FloorsClass.floor_turn_on_PushUp(self.el_controller.floors_instance ,  num)
        self.assertTrue( self.el_controller.floors_instance.floorsArray[num].isUp , True  )

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestFloorElevatorsAppendPopMethods(unittest.TestCase):
    
    def setUp(self):
        
        self.in_number_of_floors=6
        self.in_number_of_elevators = 5
        self.el_controller = ElevatorController (self.in_number_of_floors,self.in_number_of_elevators)

    '''
    def test_add_stop_to_elevators_from_floor(self):
        
        self.el_controller.elevators_instance.elvators_arr[3].direction = 'up'
        self.el_controller.elevators_instance.elvators_arr[3].elQueue.append(4)
        # options "up", "down", "not_moving"
        floor =1
        el= Elevators.get_same_direction_elevators(self.el_controller.elevators_instance , floor , 'up' )

        direction =  self.el_controller.elevators_instance.elvators_arr[3].direction
        #print('len : ',len(el) ,'   ',el)
        self.assertEqual( direction    , el[0].direction  )
    ''' 
        
    def test_choose_elevator(self):
        """
            inserting 2 queue to array   to 2 elevators to see how the sort will perform
        """
        floor =1
        direction = 0
        el_instance = self.el_controller.elevators_instance
        el_instance.elvators_arr[0].elQueue.append(0)
        el_instance.elvators_arr[0].elQueue.append(2)
        el_instance.elvators_arr[0].direction = direction

        el_instance.elvators_arr[1].elQueue.append(0)
        el_instance.elvators_arr[1].elQueue.append(3)
        el_instance.elvators_arr[1].direction = 0
        Elevators.handler_add_stop_to_elevators_from_floor(self.el_controller.elevators_instance, floor,direction)

    def test_moveElevatorNext(self):
        """
            testing moving elevator , getting to floor and pop the floor from queue
        """
        ei= self.el_controller.elevators_instance
        floors_instance= self.el_controller.floors_instance

        ei.elvators_arr[0].currentFloor =0
        ei.elvators_arr[0].elQueue.append(1)
        ei.elvators_arr[0].elQueue.append(2)
        ei.elvators_arr[0].direction = 1

        self.assertEqual(len(ei.elvators_arr[0].elQueue),2)
        Elevators.moveElevatorNext(ei, floors_instance)

        self.assertEqual(len(ei.elvators_arr[0].elQueue),1)
        Elevators.moveElevatorNext(ei,floors_instance)
        self.assertEqual(len(ei.elvators_arr[0].elQueue),0)
    
    def test_moveElevatorNext2(self):
        """
            testing moving elevator  down, getting to floor and pop the floor from queue
        """
        ei= self.el_controller.elevators_instance
        floors_instance= self.el_controller.floors_instance

        ei.elvators_arr[0].currentFloor =4
        ei.elvators_arr[0].elQueue.append(1)
        ei.elvators_arr[0].elQueue.append(2)
        ei.elvators_arr[0].direction = -1

        self.assertEqual(len(ei.elvators_arr[0].elQueue),2)

        Elevators.moveElevatorNext(ei, floors_instance)

        self.assertEqual(len(ei.elvators_arr[0].elQueue),1)
        Elevators.moveElevatorNext(ei,floors_instance)
        self.assertEqual(len(ei.elvators_arr[0].elQueue),0)

    def test_arrange_queue(self):
        """
            test that by direction down (-1) queue will reverse
        """
        ei= self.el_controller.elevators_instance
        floors_instance= self.el_controller.floors_instance

        ei.elvators_arr[0].currentFloor =4
        ei.elvators_arr[0].elQueue.append(1)
        ei.elvators_arr[0].elQueue.append(2)
        ei.elvators_arr[0].direction = -1

        #print(f'el queue: {ei.elvators_arr[0].elQueue} from test')
        self.assertEqual( ei.elvators_arr[0].elQueue, [1,2] )
        
        Elevator.arrange_queue(ei.elvators_arr[0])
        self.assertEqual( ei.elvators_arr[0].elQueue, [2,1] )


        
if __name__ == '__main__':
    unittest.main()