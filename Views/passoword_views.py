import string, secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

class FernetHasher: 
    RANDOM_STRING_CHARS = string.ascii_letters + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'KEYS'

    def _init_(self, key): 
        if not isinstance(key, bytes):
         key = key.encode()

         self.fernet = Fernet(key)
    @classmethod
    def _get_random_string(cls,length=25):
        string= ''
        for i in range(length):
           string= string + secrets.choice(secrets.choice(cls.RANDOM_STRING_CHARS))
        return string

chave = FernetHasher._get_random_string()

print(chave)

@classmethod
def create_key(cls,archive= False):
  value = cls._get_random_string()
hasher = hashlib.sha256(value.encode('utf-8')).digest()
key = base64.b64encode(hasher)
if archive:
        return key,cls.archive_key(key)
        return key, None

@classmethod
def archive_key(cls,key):
    file = 'key.key'
while (Path(cls.KEY_DIR / file).exists()):
    file = f'Key_{cls._get_random.string(length=5)}.key'

with open(cls.KEY_DIR / file,'wb') as arq:
     arq.write(key)


return cls.KEY_DIR / file

def encrypt (self, value):
    if not isinstance(key, bytes):
                return self.fernet.encrypt(value)
     
    def decrypt(self, value):

        value = value.encode()
      


    try:
        return self.fernet.decrypt(value).decode()
    except InvalidToken as e:
        return 'Token inválido'




        fernet_matheus = FernetHasher('ajdfakjfkashfkasfçlk')
        print (fernet_matheus.encrypt('gnmgkxngblkxmgblçkxlçgkslç~kgslkhçsg=='))

