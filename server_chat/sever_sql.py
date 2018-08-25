import sqlite3 
import sys
import os
import time
import socket

class ConnectSQL:
    path ="db.db" # l
    con = sqlite3.connect(path)    # connect 
    cur = con.cursor()
    def Open(self):
        ConnectSQL.path ="db.db" #lay ten file cong voi bien
        ConnectSQL.con = sqlite3.connect(ConnectSQL.path)   
        ConnectSQL.cur = self.con.cursor()
        print ("successfuly!\n")
        
    def SignUp(self,username, password,birthday,city):
        cur = ConnectSQL.con.cursor() 
        cur.execute("insert into user1 (username, password,birthday,city) values (?,?,?,?)", (username, password,birthday,city)) 
       # cur.commit()
        drec = "successfuly"
        return drec
    def CheckCity(self,city):
        hascity = 0
        cur = ConnectSQL.con.cursor() 
        cur.execute("SELECT idc FROM city WHERE name = ? ", (city,) )
        row = cur.fetchone()
        if row != None:
            hascity = 1
        return hascity
    
  #  def WriteToCity(self,name):
    #    sql = "INSERT INTO city(name) VALUES(?) "
        
        ConnectSQL.cur.execute(sql,(name,)) 
    def TranCityToId(self,name):
        sql = "SELECT id FROM user1 WHERE username = ?"
        self.cur.execute(sql,(name,))
        row = self.cur.fetchone()
        return row[0]
    
    def CheckSignIn(self,us, pas):
        sql = "SELECT * FROM  user1 WHERE username = ? and password = ?"
        self.cur.execute(sql,(us,pas))
        row = self.cur.fetchone()
        if row == None :
            return -1
        return row[0] # hien thi
    
    #----------------------------------------------------------------------
    def ShowMessDetail(self,id1,id2):
        sql = "SELECT * FROM (SELECT * FROM messenger WHERE (idsen = ? AND idrec = ?)  ) AS B LEFT JOIN  user1 ON (user1.id = B.idsen )"
        self.cur.execute(sql,(id1,id2))
        row = self.cur.fetchone()
        drec = ""
        while row!= None:
            name = row[6]
            mess = row[2]
            time_mess = row[3]
            sta = row[4] 
            drec = drec +name + "," + mess + "," + time_mess + ","
            row= self.cur.fetchone()
        return drec
    #--------------------------------------------------------------------------
    def ShowMessSen(self,id1,id2):
        sql = "SELECT * FROM (SELECT * FROM messenger WHERE (idsen = ? AND idrec = ?)  ) AS B LEFT JOIN  user1 ON (user1.id = B.idrec )"
        self.cur.execute(sql,(id1,id2))
        row = self.cur.fetchone()
        while row!= None:
            print (row[6])
            print ("      ",row[2])
            print ("               ",row[3])
            sta = row[4] 
            if sta == 1:
                print("                     đã xem")
            if sta == 0:
                print("                     Chưa đọc")
            row= self.cur.fetchone()
    #---------------------------------------------------------------------------
    def WriteToMess(self,id1,id2,mess,dt):
        cur = ConnectSQL.con.cursor() 
        sql = "INSERT INTO messenger VALUES (?,?,?,?,0)"
        self.cur.execute(sql,(id1,id2,mess,dt))
        print("Đã giửi")
    def Showfriend(self,id):
        """"""
#       cur = ConnectSQL.con.cursor()
        print (id,"-------List Friends-----------\n")
        sql = "SELECT DISTINCT user1.username FROM (SELECT * FROM Friend where id1 = ?  AND isblock = 0) as A LEFT JOIN user1 ON (A.id2 = user1.id) ORDER BY timeadd ASC "
        self.cur.execute(sql,(id,))
        row = self.cur.fetchone()
        drec = ""
        while row!= None:
            
            a = row[0]
            drec = drec + a + ","
            row= self.cur.fetchone()
        return drec 
    #----------------------------------------------------------------------
    def TranNameToId(self,name):
        sql = "SELECT id FROM user1 WHERE username = ?"
        self.cur.execute(sql,(name,))
        row = self.cur.fetchone()  
        if row == None:
            return -1
        return row[0]
    
    #----------------------------------------------------------------------
    def CheckBlock(self,id1,id2):
        """"""
        isblock = 0
        sql = "SELECT RelationshipStatus FROM Friend WHERE (id1 = ? AND id2 = ?) OR (id1 = ? AND id2 = ?)"
        self.cur.execute(sql,(id1,id2,id2,id1))
        row = self.cur.fetchone()
        isblock = row[0]
        return isblock
    
    #----------------------------------------------------------------------
    def ShowCity(self,name):
        sql = "SELECT id FROM user1 WHERE username = ?"
        self.cur.execute(sql,(name,))
        row = self.cur.fetchone()  
        if row == None:
            return -1
        return row[3]
    #----------------------------------------------------------
    def AddFriend(self,id1,id2,city,dt):
        cur = ConnectSQL.con.cursor() 
        sql ="INSERT INTO friend VALUES (?,?,0,?,?)"
        self.cur.execute(sql,(id1,id2,city,dt))
        
    #----------------------------------------------------------------------
    def UpdateStatusfriend(self,status,id1,id2):
        who = 0
        if status == 1:
            who = id1
        sql = "UPDATE Friend SET RelationshipStatus = ? , whoblock = ? WHERE (id1 = ? AND id2 = ?) OR (id1 = ? AND id2 = ?)"
        cur = ConnectSQL.con.cursor() 
        self.cur.execute(sql,(status,who,id1,id2,id2,id1))
        
    #----------------------------------------------------------------------
    def CheckWhoBlock(self,id1,id2):
        """"""
        whoblock = 0
        sql = "SELECT whoblock FROM Friend WHERE (id1 = ? AND id2 = ?) OR (id1 = ? AND id2 = ?)"
        self.cur.execute(sql,(id1,id2,id1,id2))
        row = self.cur.fetchone()
        whoblock = row[0]
        return whoblock
    
    #----------------------------------------------------------------------
    def CheckFriend(self,id,id2):
        """"""
        sql = "SELECT * FROM Friend WHERE ( id1 = ? AND id2 = ?) OR ( id1 = ? AND id2 = ?)"
        self.cur.execute(sql,(id,id2,id2,id))
        row = self.cur.fetchone()
        if row is not None:
            return 1
        return 0
    
    #----------------------------------------------------------------------
    def WriteToFriend(self,id1,id2):
        """"""
        sql = "INSERT INTO Friend VALUES (?,?,?,?,?)"
        import time
        localtime = time.asctime(time.localtime(time.time()))
        self.cur.execute(sql,(id1,id2,localtime,0,0))
        drec = "successfuly"
        return drec
    #----------------------------------------------------------------------
    def ShowFriendByCity(self,id):
        """"""
        dic = dict()
        sql = "SELECT city.idc,User.id FROM city, User,Friend WHERE (Friend.id1 = ? or Friend.id2 = ?) and (User.id = Friend.id1 or User.id = Friend.id2)  and User.city = city.idc and User.id != ?"
        self.cur.execute(sql,(id,id,id))
        row = self.cur.fetchone()
        while row != None:
            dic[row[0]] = {row[1]}
            row= self.cur.fetchone()
        
        
        
