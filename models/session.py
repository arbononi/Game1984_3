from models.models import Usuario

class Session:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.user = None
        return cls._instance
    
    def login(self, user: Usuario):
        self.user = user

    def logoff(self):
        self.user = None

    def is_logged_in(self):
        return self.user is not None