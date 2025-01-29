import os
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESManager:
    def __init__(self, key=None):
        self.key = key or os.urandom(32) # Clé AES 256 bits

    def encrypt_message(self, message):
        iv = get_random_bytes(16)  # Vecteur d'initialisation
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded_message = pad(message.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return iv + ciphertext  # Combinaison de l'IV et du texte chiffré

    def decrypt_message(self, ciphertext, key):
        cle = key or self.key
        iv = ciphertext[:16]  # Extraire l'IV
        cipher = AES.new(cle, AES.MODE_CBC, iv)
        decrypted_padded_message = cipher.decrypt(ciphertext[16:])
        return unpad(decrypted_padded_message, AES.block_size).decode()

    def get_key(self):
        return self.key


# Utilisation
# Instanciation du classe de cryptage AESManager
# manager = AESManager()
#
# # Le message à crypter
# message = "Hello, dada!"
#
# # crypter le message et l'affecter dans la variable encrypted
# encrypted = manager.encrypt_message(message)

# encoder en hexadecimale pour qu'il soit plus lisable
# hexaText = base64.b64encode(encrypted).decode('utf-8')
#
# # Obtenir la cle et aussi l'encoder en hexadecimale
# key = base64.b64encode(manager.get_key()).decode('utf-8')
# print("Encrypted:", hexaText, key)
#
# # Retransformer en binaire la cle et le texte
# decoder = base64.b64decode(hexaText)
# k = base64.b64decode(key)
#
# # decrypter le message avec la cle de dechiffrement
# decrypted = manager.decrypt_message(decoder,k)
# print("Decrypted:", decrypted)
