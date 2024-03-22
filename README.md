# **LAPORAN PRAKTIKUM PEMROGRAMAN JARINGAN “Client – Server (Single Thread)”**

Nama : Hammam Jauharul Karim

NIM : 1203222050

## Soal Nomer 1
1.	Membuat sebuah program server yang dapat menerima koneksi dari klien menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 12345 untuk server. Membuat analisa dari hasil program tersebut

Screenshot :
![3](https://github.com/hammamkarim/Pemrograman_Jaringan/assets/114963944/de248303-8573-443a-a8d8-251e246b404e)


![Screenshot 2024-03-20 181118](https://github.com/hammamkarim/Pemrograman_Jaringan/assets/114963944/ec06bea6-42cc-40e0-be2c-3af6b9fbb32f)


### Analisa Code

Program tersebut adalah implementasi dari server socket menggunakan modul socket. Ini adalah server yang sederhana yang akan menerima koneksi dari klien, mengirimkan pesan ke klien, dan kemudian menutup koneksi. Adapun penjelasan singkat mengenai baris code tersebut kurang lebih sebagai berikut :

•	import socket : Mengimpor modul socket yang digunakan untuk berkomunikasi melalui jaringan menggunakan socket.

•	def main() : Mendefinisikan fungsi utama main().

•	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): 
Membuat objek soket untuk server dengan menggunakan alamat IPv4 (AF_INET) dan tipe soket stream (SOCK_STREAM).

•	server_socket.settimeout(10) : Mengatur waktu tunggu (timeout) untuk soket menjadi 10 detik. Ini berarti jika tidak ada koneksi baru dalam waktu 10 detik, maka socket akan melemparkan pengecualian.

•	server_address = ('localhost', 12345) : Menentukan alamat dan port server. Dalam hal ini, server berjalan di localhost (127.0.0.1) pada port 12345.

•	server_socket.bind(server_address) : Mengikat (bind) socket server ke alamat dan port yang telah ditentukan sebelumnya.

•	server_socket.listen(2) : Listen koneksi dari klien. Parameter 2 menentukan bahwa server dapat menerima hingga 2 koneksi klien secara bersamaan.

•	print(f'Server listening on {server_address}...') : Mencetak pesan bahwa server sedang tersambung pada alamat dan port tertentu.

•	while True: : Memulai loop tak terbatas untuk menerima koneksi dari klien.

•	client_socket, client_address = server_socket.accept() : Menerima koneksi baru dari klien dan mendapatkan objek soket klien serta alamat klien.

•	received_data = client_socket.recv(1024) : Menerima data yang dikirimkan oleh klien dengan maksimal 1024 bytes.

•	message = f'Menerima {len(received_data)} bytes: {received_data.decode()}' : Membuat pesan yang berisi jumlah byte yang diterima dan isi pesan yang diterima dari klien.

•	client_socket.sendall(response.encode()) : Mengirimkan respons kembali kepada klien. Respons ini berupa jumlah karakter dari pesan yang diterima.

•	client_socket.close() : Menutup koneksi dengan klien saat selesai 
berkomunikasi dengan klien tersebut.
•	except socket.timeout : Menangkap pengecualian jika timeout terjadi.

•	Finally : Bagian akhir yang akan dieksekusi terlepas dari apakah ada pengecualian atau tidak.

•	server_socket.close() : Menutup soket server.

### Analisa Hasil

•	Menampilkan pesan "Server listening on localhost:12345..." saat server siap menerima koneksi.

•	Menampilkan pesan "Menerima koneksi dari client_address" saat menerima koneksi dari client.

•	Menampilkan pesan "Menerima ... bytes: ..." dan "Kirim Respon: ..." setiap kali menerima pesan dari client dan mengirim respons ke client.

•	Menampilkan pesan "Batas waktu socket telah habis, mohon sambungkan kembali" jika terjadi timeout.

•	Menampilkan pesan kesalahan jika terjadi exception.

## Soal Nomer  2 

2.	Membuat sebuah program klien yang dapat terhubung ke server yang telah dibuat pada soal nomor 2. Klien ini akan mengirimkan pesan ke server berupa inputan dari pengguna dan menampilkan pesan balasan jumlah karakter yang diterima dari server. Membuat analisa dari hasil program tersebut

Screenshot :

![4](https://github.com/hammamkarim/Pemrograman_Jaringan/assets/114963944/3b40d80a-4c7c-4992-b777-1e7482123f25)


![Screenshot 2024-03-20 181101](https://github.com/hammamkarim/Pemrograman_Jaringan/assets/114963944/51c949a7-35a8-4df6-990f-c90453c7228b)





