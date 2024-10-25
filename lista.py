from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib

# URI de conexão com o MongoDB
uri = "mongodb+srv://guilherme12062008:gui120608@cluster.bwarq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

# Cria um novo cliente e conecta ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Envia um ping para confirmar uma conexão bem-sucedida
try:
    client.admin.command('ping')
    print("Pingou seu servidor. Conexão bem-sucedida com o MongoDB!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

# Solicita a senha do usuário
senha = input("Digite sua senha: ")

# Cria um objeto sha256 e gera o hash
sha_signature = hashlib.sha256(senha.encode()).hexdigest()

# Exibe a senha original e o hash gerado
print(f"Senha original: {senha}")
print(f"Hash SHA-256: {sha_signature}")
