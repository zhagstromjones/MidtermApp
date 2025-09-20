from cryptography.fernet import Fernet
import hashlib

key = Fernet.generate_key()
fernet = Fernet(key)

# Write a message and ensure its integrity
hash1 = hashlib.sha256()
message = input("Input a message: ")
hash1.update(bytes(message, 'utf-8'))
print("SHA256 hash: " + hash1.hexdigest())

# Encrypt message with key
encryptedMessage = fernet.encrypt(message.encode())
print("Ciphertext: ", encryptedMessage)

# Decrypt the message
decryptedMessage = fernet.decrypt(encryptedMessage).decode()
print("Decrypted plaintext: ", decryptedMessage)

# Verify message integrity
hash2 = hashlib.sha256()
hash2.update(bytes(message, 'utf-8'))
print("SHA256 hash: " + hash2.hexdigest())

if hash2.hexdigest() != hash1.hexdigest():
    print("Hash mismatch")
else:
    print("Hash match")
