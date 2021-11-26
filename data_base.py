import mysql.connector
from functions import user_db

class Data_base(object):
    def __init__(self, user, passwd):
        self.db = mysql.connector.connect(user = user, passwd = passwd, db = 'gastometro', host='dados.com')
        self.cursor = self.db.cursor()

    def register_user(self, user, name):
        self.cursor.execute('insert into user (nick, name) values ("%s", "%s")' %(user, name))
        self.db.commit()

    def basic_request(self, table, column = '*', order_by = ''):
        if order_by == '': self.cursor.execute('select %s from %s' %(column, table))
        else: self.cursor.execute('select %s from %s order by %s' %(column, table, order_by))
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

    def regist(self, owner, date, title, detais, value, _type, _class):
        self.cursor.execute('insert into register (owner, date, title, detais, value, type, class) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' %(owner, date, title, detais, value, _type, _class))
        self.db.commit()
    
    def update_regist(self, _id, date, title, detais, value, _type):
        self.cursor.execute('update register set date = "%s", title = "%s", detais = "%s", value = "%s", type = "%s" where id = %s' %(date, title, detais, value, _type, _id))
        self.db.commit()

    def get_register(self):
        register = []
        for i in self.basic_request('register', 'owner, date, title, value, type, id, class', 'date'): register.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        return register

    def get_data_by_id(self, _id):
        self.cursor.execute('select * from register where id = %s' %_id)
        for i in self.cursor: data = ([i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0]])
        return data

    def delete_registers(self, regist):
        self.cursor.execute('delete from register where id = %s' %regist)
        self.db.commit()

    def calc_balance(self):
        response = 0.00
        for i in self.basic_request('register', 'type, value'):
            if i[0] == 'si': response -= float(i[1])
            elif i[0] == 'en': response += float(i[1])
        return ('%.2f' % response)

if __name__ == "__main__":
    user = user_db()
    db = mysql.connector.connect(user = user[0], passwd = user[1], host='dados.com')
    cursor = db.cursor()
    try:
        cursor.execute('create database gastometro')
    except:
        cursor.execute('drop database gastometro')
        cursor.execute('create database gastometro')
    cursor.execute('use gastometro')
    cursor.execute('create table user (nick varchar(20) primary key, name varchar(50))')
    cursor.execute('create table register (id int(191) primary key auto_increment, owner varchar(20), date varchar(191) not null, title varchar(20) not null, detais varchar(191) not null, class varchar(2) default "cp", value varchar(191), type varchar(2) not null)')