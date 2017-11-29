import socket   #for sockets
import sys

host="localhost"
port=4444

def main():
    try:
        # Creating  socket PIv4 using TCP protocol
        print("Initializing socket...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err_msg:
        print("Unable to instantiate socket.")
        print("Error code: " + str(err_msg[0]))
        print("Error message : " + err_msg[1])
        sys.exit();

    print("Initializing socket...done")

    print("Binding socket...")
    sock.bind((host, port))

    print("Binding socket...done")

    print("Listenning on port " + str(port))
    sock.listen(1)

    print("Accepting socket...")
    s, address = sock.accept()
    print("Accepting socket...done")

    print("Connection from: " + str(address))

    while True:
        # Receving data
            data = s.recv(256)
        # Checking if data is null
            if not data:
            # Close session
                break
        # Printing data
            print(data)
        # Waiting for a string input
            data = raw_input("# ")
        # Sending data
            s.send(data)
    # Closing socket
    print("Closing socket...")
    s.close()
    print("Closing socket...done")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
        sys.exit()
