from flask import session

class AuthMiddleware:
    
    @staticmethod
    def is_logged():
        return 'id' in session
    
    @staticmethod
    def get_employee_permission():
        return session['tipo'] == 'funcionario'