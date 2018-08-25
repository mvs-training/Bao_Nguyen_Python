import socket
HOST = 'localhost'    # Cấu hình address server
PORT = 8000
class Client_server:
	
	def __init__(self):
		self.id = 1
		self.username = 1
		self.password = 1
		self.bitrhday = 1
		self.city = 1
		self.flag = None
        
	def SignUp_cl(self):
              # Cấu hình Port sử dụng
		print(" -- tao tai khoan dang nhap -- \n")
		print("tao tai khoa")
		username = input()
		print (type(username))
		print("tao mat khau ")
		password = input()
		print("tao ngay sinh")
		bitrhday = input()
		print("tao thanh pho ")
		city = input()
		clien_sen=""
		clien_sen=clien_sen+username+","+password+","+bitrhday+","+city
		print(username,password,bitrhday,city, "hien hi thu \n")
		return clien_sen

	def SignIn_cl(self):
		print("dang nhap tai khoan \n")
		username = input()
		print (type(username))
		print("nhap mat khau ")
		password = input()
		client_sen = ""
		client_sen = clien_sen+username+","+password
		print(username,password,"hien hi thu \n")
		return client_sen
	def ShowMess_cl(self):
		if self.flag == 1:
			print("hien thi tin nhan")
			print("gưi lại ấn 1 thoát ấn 2\n")
			chon = int(input())
			if chon == 1:
				print("lựa chọn 1:\n")
			if chon == 2:
				print("lựa chọn 2: \n")

		if self.flag != 1:
			print("bạn chưa đăng nhập.\n")
		return client_sen
	def SenMess_cl(self):
		senmess = input("soan tin nhan\n")
		client_sen = ""
		client_sen = client_sen + senmess
	def frien(self):
		frien = input("nhap ten ban be")
		client_sen = ""
		client_sen = client_sen +self.username+","+frien
		return client_sen
	def AddFriend_cl():
		print("phần thêm bạn bè")
	def ShowFriend_cl():
		print("phần hiển thị bạn bè")