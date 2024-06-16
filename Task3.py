import numpy as np
import random

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    encrypted_vector = np.dot(key_matrix, message_vector)
    return encrypted_vector

def decrypt_message(encrypted_vector, key_matrix):
    key_matrix_inv = np.linalg.inv(key_matrix)
    decrypted_vector = np.dot(key_matrix_inv, encrypted_vector)
    decrypted_message = ''.join([
        chr(int(np.round(num))) for num in decrypted_vector
        if 0 <= int(np.round(num)) < 0x110000
    ])
    return decrypted_message

words = ["Hello, World!", "Python", "Encryption", "Random", "Message", "Test", "Example"]

original_message = random.choice(words)
key_matrix_size = len(original_message)
key_matrix = np.random.randint(1, 10, (key_matrix_size, key_matrix_size))

print(f"Original Message: {original_message}")

encrypted_message = encrypt_message(original_message, key_matrix)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, key_matrix)
print(f"Decrypted Message: {decrypted_message}")

if original_message == decrypted_message:
    print("The decryption was successful!")
else:
    print("The decryption failed.")
