class User:
    def __init__(self,username,password):
        self.username=username
        self.__password = password

    def guest_id(self):
        print(f"guest id created {self.username}")

    def delate(self):
        print(f"user delate the account {self.username}")

    def password_correct(self):
        print(f"user passwored correct {self.__password}")

a=User("manju","name123")
a.guest_id()
a.password_correct()


