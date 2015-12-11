#!/usr/bin/env python3

import sys
import argparse

import time
import socket
from socket import socket as Socket

def main():

    # Command line arguments. Use a server_port > 1024 by default so that we can run
    # server without sudo.
    parser = argparse.ArgumentParser()

    parser.add_argument('--server-port', '-p', default=2081, type=int,
                        help='Server_Port to use')

    parser.add_argument('--run-server', '-s', action='store_true',
                        help='Run a ping server')

    parser.add_argument('server_address', default='localhost',
                        help='Server to ping, no effect if running as a server.')

    parser.add_argument('--packts','-q', default=10,type=int,
                        help='How many packts you want send.')

    args = parser.parse_args()


    if args.run_server:
        return run_server(args.server_port)
    else:
        return run_client(args.server_address, args.server_port, args.packts)




def run_server(server_port):
    """Run the UDP pinger server
    """

    # Create the server socket (to handle UDP requests using ipv4), make sure
    # it is always closed by using with statement.
    with Socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:

        # The socket stays connected even after this script ends. So in order
        # to allow the immediate reuse of the socket (so that we can kill and
        # re-run the server while debugging) we set the following option. This
        # is potentially dangerous in real code: in rare cases you may get junk
        # data arriving at the socket.
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Set the server port
        server_socket.bind(('', server_port))

        # Start accepting ping requests
        print("Ping server ready on port", server_port)
        while True:
            # Receive message and send one back
            _, client_address = server_socket.recvfrom(1024)
            server_socket.sendto("sdfg".encode(), client_address)

    return 0


def run_client(server_address, server_port, packts):
    """Ping a UDP pinger server running at the given address
    """

    #Create a socket UTP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        cont = 1
        while(cont <= packts):

	        #Stat the time when send the data to the server
	        start_time = time.time()

                # Connect to server and send data
	        sock.sendto("".encode(), (server_address, server_port))

	        # receive data from client (data, addr)
	        d = sock.recvfrom(1024)

	        #Count how many time was spend for receve the data
	        elapsed_time = time.time() - start_time

	        #Get the server address
	        server_addr = d[1]

	        #If the time is less than 1, print the pong
	        if  elapsed_time < 1:
        	        print ("ping",cont, "1024 bytes", "From:", server_addr ,"RTT:"  ,round(elapsed_time*1000, 3), "ms")

	        if  elapsed_time > 1:
                        print("ping",cont, "Time out")

	        cont = cont + 1

    finally:
        sock.close()



    return 0

if __name__ == "__main__":
    sys.exit(main())
