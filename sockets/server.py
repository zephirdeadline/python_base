
import socket
import sys
from threading import Thread


def test_size_data(data, max_size):
    siz = sys.getsizeof(data)
    if siz >= max_size:
        print("The length of input is probably too long: {}".format(siz))


def do_some_stuffs_with_input(input_string):
    print("Processing that nasty input!", input_string)
    return input_string


def client_thread(conn, ip, port, client_list, max_size=4096):
    while True:
        data = conn.recv(max_size)
        if not data:
            break

        data = data.decode("utf8")
        do_some_stuffs_with_input(data)
        data += str(len(client_list))
        data = data.encode("utf8")
        conn.sendall(data)
    conn.close()

    print('Connection ' + ip + ':' + port + " ended")


class Client:
    def __init__(self, ip, port, conn, name=""):
        self.port = port
        self.ip = ip
        self.conn = conn
        self.name = name


def start_server():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("", 12345))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    soc.listen(10)
    print('Socket now listening')

    client_list = []
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        new_client = Client(ip, port, conn)
        client_list.append(new_client)
        print('Accepting connection from ' + ip + ':' + port)
        for client in client_list:
            if id(client) != id(new_client):
                client.conn.sendall(f"A new client just connected! id: {id(client)}".encode('utf8'))
        try:
            Thread(target=client_thread, args=(conn, ip, port, client_list)).start()
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
    soc.close()


start_server()