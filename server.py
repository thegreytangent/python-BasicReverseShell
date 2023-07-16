import socket
import sys

# Creating a socket to connect 2 computers
def create_socket():
    try: 
        global host
        global port
        global s
        host = ""
        port = 9999;
        s = socket.socket()
    except socket.error as msg:
        print("socket error" + str(msg));

#Binding the socket and listening connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port " + str(port))

        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket error" + str(msg)+" Retrying")
        bind_socket()

# Establis connection with a client should listen
def socket_accept():
   conn, address =  s.accept()
   print("Connection  has been establish. IP: " + address[0]+" and Port: " + str(address[1]) )
   send_command(conn)
   conn.close()
    

#send commands    
def send_command(conn) :
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()