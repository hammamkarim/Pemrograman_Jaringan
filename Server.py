# Server
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(10)
    server_address = ('localhost', 12345)
    
    try:
        server_socket.bind(server_address)
        server_socket.listen(2)
        print(f'Server listening on {server_address}...')
        
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print(f'Menerima koneksi dari {client_address}')
                
                received_data = client_socket.recv(1024)
                message = f'Menerima {len(received_data)} bytes: {received_data.decode()}'
                print(message)
                
                response = f'Jumlah karakter: {len(received_data)}'
                client_socket.sendall(response.encode())
                print(f'Kirim Respon: {response}')
                
                client_socket.close()
                
            except socket.timeout:
                print('Batas waktu socket telah habis, mohon sambungkan kembali')
                continue
            except Exception as e:
                print(f'Error {e}')
                break
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
