from model.password import password
from views.password_views import Fernethasher
import sys,os

sys.path.append(os.path.abspath(os.curdir))


from model.password import Password
from views.password_views import FernetHasher

action = input('Digite um para salvar uma nova senha ou 2 para ver uma senha salva')

if action == '1':
    if len(password.get()) == 0:
        key,path = FernetHasher.create_key(archive=true)
        print('Sua chave foi criada com sucesso, salve-a com cuidado')
        print(f'chave:{key.decode("utf-8")}')
        if path:
            print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
            print(f'caminho: {path}')
        else:
            key= input('Digite sua chave usada para criptografia, use sempre para a mesma chave:')



            domain = input('Dominio:')
            Password = input('Senha')
            fernet_user = FernetHasher(key)
            p1 = password(domain, password=fernet_user.encrypt(password).decode('utf-8'))
            p1.save()

elif action == '2'
domain = input('dominio:')
key = input ('key:')
fernet_user = FernetHasher(key)
data = password.get()


for i in data:
    if domain in i ['domain']:
       password = fernet_user_decrypt(i['passord'])

    if password:
        print('f Sua senha: {password}' )
    else:
        print('Nenhuma senha encontrada para o dominio')