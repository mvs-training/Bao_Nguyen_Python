from Client_server import Client_server 
#import  Client_user
import socket
HOST = 'localhost'    # Cấu hình address server
PORT = 8400              # Cấu hình Port sử dụng

def main():
	cl = Client_server()
	while True:
		print("1 : tạo tài khoản  \n2 : đăng nhâp \n3 : hiện bạn bè \n4 : sau tin đến \n5 : hiển thị tin nhắn gửi đi \n6 : gửi tin nhắn\n")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
		s.connect((HOST, PORT)) # tiến hành kết nối đến server
		print("da ket noi voi server\n")

		chose = int(input("nhap vao 1 lua chon\n"))
		if chose == 1:
			# tao tai khoan
			data = cl.SignUp_cl()
			data ="a," + data
			s.sendall(data.encode()) # Gửi dữ liệu lên server
			data = s.recv(1024) # Đọc dữ liệu server trả về
			if len(data) > 0:
				print(data)
		if chose == 2:
			#dang nhap
			data = cl.SignIn_cl()
			data = "aa,"+ data
			s.sendall(data.encode()) # Gửi dữ liệu lên server
			data = s.recv(1024) # Đọc dữ liệu server trả về
			if len(data) > 0:
				print(data)
		if chose == 3:
			#hien ban be
			#s.sendall(data.encode()) # Gửi dữ liệu lên server
			data= cl.frien()
			data = "aaaa,"+data
			s.sendall(data.encode()) # Gửi dữ liệu lên serve
			s.sendall(data.encode()) # Gửi dữ liệu lên serve
			data = s.recv(1024)
			Data=data.decode()
			frien=data.split(",")
			i = 0
			while kt > 0:
				if len(frien[i]) > 0:
					print(frien[i])
					i = i + 1
				elif len(frien[i]) <= 0:
					kt = 0
		if chose == 4:
			#hien tin da gui
			data= cl.frien()
			data = "aaaa,"+data
			print("aaa,")
			s.sendall(data.encode()) # Gửi dữ liệu lên serve
			data = s.recv(1024)
			Data=data.decode()
			mess=data.split(",")
			i = 0
			while kt > 0:
				if len(mess[i]) > 0:
					print(mess[i])
					print("      ",mess[i+1])
					print("                 ",mess[i+2])
					i = i + 3
				elif len(mess[i]) <= 0:
					kt = 0
		if chose == 5:
			#gui tin nhan
			data= cl.frien()
			data = "aaaaa,"+data+","+cl.SenMess_cl()
			s.sendall(data.encode()) # Gửi dữ liệu lên server
			data = s.recv(1024) # Đọc dữ liệu server trả về
			if len(data) > 0:
				print(data)
			#s.sendall(data.encode()) # Gửi dữ liệu lên server
			#us.SenMess(us.id)
		if chose == 6:
			#then ban
			data= cl.frien()
			data = "aaaaaa,"+data
			s.sendall(data.encode()) # Gửi dữ liệu lên serve
			#s.sendall(data.encode()) # Gửi dữ liệu lên server
			data = s.recv(1024) # Đọc dữ liệu server trả về
			if len(data) > 0:
				print(data)
			#us.AddFriend(us.id)
		if chose == 7:
			print("thoat")
			return 0
			#s.sendall(data.encode()) # Gửi dữ liệu lên server
			#us.ShowFriend(us.id)
		s.close() #dong socket
if __name__ == '__main__':
	main()