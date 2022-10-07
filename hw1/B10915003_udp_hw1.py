from os import system
import socket
import time

#dest ip
DEST_IP = "127.0.0.1"
#port number
PORT = 5005
#Student ID
STUID = "B10915003"
#Send Times
SEND_TIMES = 10

#Create a socket
def CreateSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    return sock

#Send a message
def SendData(_data, _sock):
    _data = STUID + ":" + _data
    #create a socket
    _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #send data
    sock.sendto(bytes(_data, "utf-8"), (DEST_IP, PORT))

    print("Send To [{}]:{}=>{}".format(DEST_IP, PORT, _data))


#main
if __name__ == "__main__":
    print("========== Info ==========")
    print("Dest IP: {}".format(DEST_IP))
    print("Port: {}".format(PORT))
    print("Student ID: {}".format(STUID))
    print("Send Times: {}\n".format(SEND_TIMES))


    #create a socket
    sock = CreateSocket()

    print("========== Start ==========")
    for _ in range(SEND_TIMES):
        SendData("Hello World", sock)
        time.sleep(1)

    #close socket
    sock.close()
    system("pause")
        



