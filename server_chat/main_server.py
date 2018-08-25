from sever_sql import ConnectSQL
import sever_sql
import socket	
import socket

HOST = 'localhost' # Thiết lập địa chỉ address
PORT = 8400 # Thiết lập post lắng nghe

def main():
	sv = ConnectSQL()
	a = 5
	while a > 0 :
		print("1 : tạo tài khoản  \n2 : đăng nhâp \n3 : hiện bạn bè \n4 : sau tin đến \n5 : hiển thị tin nhắn gửi đi \n6 : gửi tin nhắn\n")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cấu hình kết nối
		s.bind((HOST, PORT)) # lắng nghe
		s.listen(1) # thiết lập tối ta 1 kết nối đồng thời
		conn, addr = s.accept() # chấp nhận kết nối và trả về thông số
		print("server hoat dong :\n")
		with conn:
			try:
		        # in ra thông địa chỉ của client
				print('Connected by', addr)
					# Đọc nội dung client gửi đến
				data = conn.recv(1024)
				Data=data.decode()
		            # In ra Nội dung
				print(Data)
				arway=Data.split(",")
				print(len(arway[0]))
					#data.decode(encoding)
					#str(b'', encoding)
				print(type(data))
				sv.Open()
				if len(arway[0]) == 1:
					# tao tai khoan
					drec = sv.SignUp(arway[1],arway[2],arway[3],arway[4])
					conn.sendall(drec.encode())

				if len(arway[0]) == 2:
					# dang nhap
					if passsv.CheckSignIn(arway[1],arway[2]) > 0:
						conn.sendall('successfuly'.encode())
				if len(arway[0]) == 3:
					# hien thi ban be
					id1 = sv.TranNameToId(arway[1])
					drec = ""
					drec = sv.ShowFriend(id1)
					conn.sendall(drec.encode())
				if len(arway[0]) == 4:
					# hien thi tin nhan
					id1 = sv.TranNameToId(arway[1])
					id2 = sv.TranNameToId(arway[2])
					drec = ""
					drec = sv.ShowMessDetail(id1,id2)
					conn.sendall(drec.encode())
					
				if len(arway[0]) == 5:
					# soan tin nhan
					id1 = sv.TranNameToId(arway[1])
					id2 = sv.TranNameToId(arway[2])
					dt = time.ctime()
					drec = sv.WriteToMess(id1,id2,arway[3],dt)
					conn.sendall(drec.encode())
				if len(arway[0]) == 6  :
					# them ban be
					id1 = sv.TranNameToId(arway[1])
					id2 = sv.TranNameToId(arway[2])
					name1=sv.ShowCity(arway[1])
					dt = time.ctime()
					drec = sv.AddFriend(id1,id2,name1,dt)
					conn.sendall(drec.encode())
			finally:
				s.close() # đóng socket
if __name__ == '__main__':
    main()
        
        
        