from app import cursor, db

def createRegister(date, title, description, type, _class, value):
    inser = "insert into registers (name, description, type, class, value, created_at) values "
    inser += "('%s', '%s', '%s', '%s', '%s', '%s')" %(title, description, type, _class, value, date)
    cursor.execute(inser)
    db.commit()

def getRegisters():
    select = "select * from registers order by created_at desc"
    cursor.execute(select)
    return cursor.fetchall()

def getBalance():
    select = "select sum(case when type = 'en' then value else value * -1 end) from registers"
    cursor.execute(select)
    return cursor.fetchall()