from loguru import logger 
class User:
    def __init__(self,ip,phone_detail,location = None):
        self.ip = ip
        self.phone_detail = phone_detail
        self.location = location

    def signup(self):
        pass

    def login(self):
        pass

    def profile_update(self):
        pass

user1 = User("10.123.1.10","Samsumg/Android","Delhi")
logger.info(f"{user1}")
logger.info(f"{user1.__dict__}")
logger.info(f"{dir(user1)}")

class Dog:
    sound ="bark"

dog1 = Dog()
logger.info(dog1.sound)