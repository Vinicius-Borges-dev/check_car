from flask import session
import imghdr

class AuthMiddleware:
    
    @staticmethod
    def is_logged():
        return 'id' in session
    
    @staticmethod
    def get_employee_permission():
        return session['tipo'] == 'funcionario'


    @staticmethod
    def image_validation(image):
        allowed = {'png','jpg','jpeg','gif'}
        realFiletype = imghdr.what(image)
        return realFiletype in allowed
        