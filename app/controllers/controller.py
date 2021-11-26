from app import app

def success(message, data = {}):
    return {
        'message': message,
        'data': data
    }