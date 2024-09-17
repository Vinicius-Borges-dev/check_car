from flask import session

class AuthMiddleware:
    
    @staticmethod
    def is_logged():
        return 'id'in session
