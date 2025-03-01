import socket
from colorama import Fore, Back, Style, init

init()


HOST = "192.168.100.11"
PORT = 9999


def sort_string(input_string, reversed=False):
    sorted_string = "".join(sorted(input_string, reverse=reversed))
    return sorted_string


def print_echo(string):
    print(Fore.CYAN + string + Style.RESET_ALL)


def print_success(string):
    print(Fore.GREEN + string + Style.RESET_ALL)


def print_error(string):
    print(Fore.RED + string + Style.RESET_ALL)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print("-----------------------------------------------------------------------\n")
print_echo("Started Listening!\n")
print("----------------------------------------------\n")


while True:
    communication_socket, address = server.accept()
    print_success(f"Connected to {address}\n")

    message = communication_socket.recv(1024).decode()

    prefix = message[0]
    string = message[1:]

    response = ""

    if prefix == "A":
        response = sort_string(string, True)
    elif prefix == "C":
        response = sort_string(string)
    elif prefix == "D":
        response = string.upper()
    else:
        response = "not a valid message"

    print("Sending response...\n")
    communication_socket.send(response.encode())
    communication_socket.close()
    print_success(f"Connection with {address} ended!\n")
    print("----------------------------------------------\n")
