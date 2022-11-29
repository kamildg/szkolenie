class userAccount:
    def __init__(self,user, passwd):
        self._username = user
        self._password = passwd

    @property
    def password(self):
        return self._password

    @password.setter
    def set_username(self, passwd):
        self._password = passwd