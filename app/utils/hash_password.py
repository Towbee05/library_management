from bcrypt import checkpw, hashpw, gensalt

# Class to hash password
class HashHelper(object):

    # Hash a password
    @staticmethod
    def hash_password(password: str) -> str:
        return hashpw(password=password.encode("utf-8"), salt=gensalt()).decode("utf-8")
    
    # Verify user password
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        if checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8")):
            return True
        return False
