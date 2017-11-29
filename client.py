import socket
import sys

host = "localhost"
port = 4444

def main():
    # Check whether socket was well instansiate
    print("Initializing socket...")
    try:
        # Creating socket IPv4 using TCP protocol
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(error)
        sys.exit()
    print("Initializing socket...done")

    # Connecting to host
    print("Connecting to host...")
    sock.connect((host, port))
    print("Connecting to host...done")

    print("\nSession opened on port " + str(port) + "\n")

    # Waiting for a string input
    data = raw_input("# ")

    # While string input differed from 'q'
    while data != 'q':
        # Sending data
            sock.send(data)
        # Receving data
            data = sock.recv(256)
        # Printing data
            print(data)
        # Waiting for a string input
            data = raw_input("# ")

    # Closing socket
    print("Closing socket...")
    sock.close
    print("Closing socket...done")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r")
        sys.exit()
