# Client
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    print(f'Connecting to {server_address}...')
    client_socket.connect(server_address)

    try:
        while True:
            message = input('Masukkan Pesan: ')
            client_socket.sendall(message.encode())

            try:
                data = client_socket.recv(1024)
                print(f'Menerima data dari server: {data.decode()}')
            except ConnectionAbortedError:
                print('Koneksi telah habis, mohon sambungkan kembali')
                break

    except KeyboardInterrupt:
        print('Koneksi Ditutup')
        client_socket.close()

if __name__ == '__main__':
    main()

