import socket
import select
import random
import pickle
import asyncio
import logging
from elevatorClass import Elevator,Elevators
from floorsClass import FloorsClass,FloorClass
import os
logging.basicConfig(level=logging.INFO)



# GLOBALS
users = {}
questions = {}
logged_users = {}  # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5678
SERVER_IP = "127.0.0.1"

def recieve_message(conn):

    data = conn.recv(4096) #.decode()
    data_variable = pickle.loads(data)
    logging.info(" server message get: ",data_variable)
    return data_variable

def send_message(conn, message):
    data_string = pickle.dumps(variable)
    logging.info(" server message send: ",data_string)
    conn.send(data_string)

# SOCKET CREATOR

def setup_socket():
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""

	print("Setting up server...")
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((SERVER_IP, SERVER_PORT))
	server_socket.listen()
	print("Listening for clients...")
	return server_socket


async def socket_controller(el_controller):
    # Initializes global users and questions dicionaries using load functions, will be used later
    global users
    global questions
    
    server_socket = setup_socket()
    client_sockets = []
    loop = asyncio.get_event_loop()
    out =False
    while True and out == False:
        await asyncio.sleep(1)
        #await loop.run_in_executor()
        ready_to_read, ready_to_write, in_error =  select.select(
            [server_socket] + client_sockets, [], [], 0.1)
        for current_socket in ready_to_read:
            if current_socket is server_socket:
                (client_socket, client_address) = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(client_socket)
            else:
                print("New data from client")
                data = recieve_message(current_socket)
                
                print(data)
                client_sockets.remove(current_socket)
                current_socket.close()
                if data['command'] == 's':
                    #server_socket.remove(current_socket)
                    server_socket.close()
                    out = True
                    os._exit(1)
                elif data['command'] == 'floor_up':
                    fl_nu = int(data['floor'])
                    FloorsClass.floor_turn_on_PushUp(el_controller.floors_instance,fl_nu )
                    Elevators.handler_add_stop_to_elevators_from_floor(el_controller.elevators_instance ,fl_nu,1)
                elif data['command'] == 'floor_down':
                    fl_nu = int(data['floor'])
                    FloorsClass.floor_turn_on_PushDown(el_controller.floors_instance,fl_nu )
                    Elevators.handler_add_stop_to_elevators_from_floor(el_controller.elevators_instance ,fl_nu,-1)
                elif data['command'] == 'el_button_press':
                    el_nu = int(data['elevator_number'])
                    fl_butt = int(data['button_number'])
                    Elevators.handler_inside_elevator_butt_press(el_controller.elevators_instance  ,el_nu,fl_butt)




# if  __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(socket_controller())
	