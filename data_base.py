import mysql.connector
from functions import user_db

class Data_base(object):
    def __init__(self, user, passwd):
        self.db = mysql.connector.connect(user = user, passwd = passwd, db = 'gastometro')
        self.cursor = self.db.cursor()

    def register_user(self, user, name):
        self.cursor.execute('insert into user (nick, name) values ("%s", "%s")' %(user, name))
        self.db.commit()

    def basic_request(self, table, column = '*'):
        self.cursor.execute('select %s from %s' %(column, table))
        return self.cursor

    def request_users(self):
        users = []
        for i in self.basic_request(table = 'user', column = 'nick'): users.append(i[0])
        return users
    
    def request_name(self, user):
        users = []
        for i in self.basic_request(table = 'user'): users.append([i[0], i[1]])
        for i in users:
            if user == i[0]: return i[1]
        return None

if __name__ == "__main__":
    user = user_db()
    db = mysql.connector.connect(user = user[0], passwd = user[1])
    cursor = db.cursor()
    try:
        cursor.execute('create database gastometro')
    except:
        cursor.execute('drop database gastometro')
        cursor.execute('create database gastometro')
    cursor.execute('use gastometro')
    cursor.execute('create table user (nick varchar(20) primary key, name varchar(50))')