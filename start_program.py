import logging
import pickle # working with dictionaries
import time
import asyncio
import random
import threading 
from elevatorClass import Elevator, Elevators
from floorsClass import FloorsClass
from  sockets.server_socket import socket_controller as sc

class ElevatorController:
    """
    controller
    """

    def __init__(self, in_number_of_floors , in_number_of_elevators):

        self.numberOfFloors = in_number_of_floors
        self.elevators_instance = Elevators( self.numberOfFloors ,in_number_of_elevators)
        self.floors_instance = FloorsClass( in_number_of_floors)


async def main( in_number_of_floors=6,in_number_of_elevators =5 ):

    el_controller = ElevatorController (in_number_of_floors,in_number_of_elevators)
    #el_controller.floors_instance.floorsArray[5].floor_turn_off_PushUp(el_controller,3)
    # await sc()
    # asyncio.run (print('###########################444#############'))
    # asyncio.run (print('###########################444#############'))
    # asyncio.create_task(sc())
    # asyncio.create_task(ee())
    await asyncio.gather(
        sc(el_controller),
        move_elevators(el_controller)
    )
    
async def move_elevators(el_controller):
    while True:
        await asyncio.sleep(5)
        #print('3333333333333333333333333')
        el_controller.elevators_instance.moveElevatorNext(el_controller.floors_instance)
        #el_controller.elevators_instance.



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(' This is an info message')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    