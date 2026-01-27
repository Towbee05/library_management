from pwdlib import PasswordHash

password_hasher= PasswordHash.recommended()

class HashHelper:
    @staticmethod
    def hash_password(plain_password: str) -> str:
        return password_hasher.hash(plain_password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return password_hasher.verify(plain_password, hashed_password)
    
