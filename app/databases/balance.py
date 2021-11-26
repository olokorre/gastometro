from app import cursor, db

def createRegister(date, title, description, type, _class, value):
    inser = "insert into registers (name, description, type, class, value, created_at) values "
    inser += "('%s', '%s', '%s', '%s', '%s', '%s')" %(title, description, type, _class, value, date)
    cursor.execute(inser)
    db.commit()