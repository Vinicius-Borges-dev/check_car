from flask import session, redirect

class AuthMiddleware:
    
    @staticmethod
    def is_logged(session):
        return 'id' in session

def getAuthResponse(func):
    def wrapper(*args, **kwargs):
        if not AuthMiddleware.is_logged(session):
            return redirect('user/')
        return func(*args, **kwargs)
    return wrapper

