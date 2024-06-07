import uuid


class UserSession:

    def __init__(self):
        self.session_id = None
        self.is_logged = False

    def login(self):
        self.is_logged = True
        self.session_id = uuid.uuid4()
        print(f"Success. You are logged in with session id: {self.session_id}")

    def logoff(self):
        self.is_logged = False
        self.session_id = None
        print(f"Success. You are logged off. Your session id expired.")

    def is_logged(self):
        if not self.is_logged:
            print(f"You are logged off.")
        else:
            print(f"You are logged in with session id: {self.session_id}")

    def get_user_data(self):
        return f"User session id: {self.session_id}, login status: {self.is_logged}."


session = UserSession()
print(session.get_user_data())
session.login()
print(session.is_logged)
session.logoff()
print(session.is_logged)
print(session.get_user_data())
