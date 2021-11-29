from app import app

def success(message, data = {}):
    return {
        'message': message,
        'data': data
    }

def loadJson(columns, data):
    list = []
    for item in data:
        json = {}
        for index in range(len(item)):
            json[columns[index]] = '%s' %item[index]
        list.append(json)

    return list