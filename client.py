import socket
import random
import string
from colorama import Fore, Style


HOST = "localhost"
PORT = 9999


CHARACTHERS = string.ascii_letters
LENGTH = 10


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

prefix = "C"
random_string = "".join(random.choice(CHARACTHERS) for _ in range(LENGTH))

message = prefix + random_string
print(Fore.CYAN + f"Message will be sent to server: " + Style.RESET_ALL + message)
socket.send(message.encode())

recieved_msg = socket.recv(1024).decode()
print(Fore.CYAN + f"Recieved message: " + Style.RESET_ALL + recieved_msg)
