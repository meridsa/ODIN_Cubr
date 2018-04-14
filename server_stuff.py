# start and listen to server

import sys
import socket
import time
import threading


def server_start(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Server socket created')
    try:
        s.bind(('', int(args[1])))  # bind socket to local host and port
    except socket.error as e:
        print('Server socket bind failed. Error Code : ' + str(e.errno))
        sys.exit()
    s.listen(10)
    print('Server now listening...')

    while 1:
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]) + ', ' + time.strftime("%Y.%m.%d  %H:%M:%S"))
        threading.Thread(target=client_thread, args=(conn, int(args[2]), int(args[3]))).start()
    s.close()


if __name__ == '__main__':  # file is executed
    if len(sys.argv) < 2:
        sys.argv.append(str(8080))  # Port 8080 default port
    if len(sys.argv) < 3:
        sys.argv.append(str(20))  # 20 moves default maximal return length of maneuver
    if len(sys.argv) < 4:
        sys.argv.append(str(3))  # 3 second default timeout for search
    print('startserver')
    server_start(sys.argv)
else:
    def start(port, maxmoves, timeout):
        server_start((-1, port, maxmoves, timeout))