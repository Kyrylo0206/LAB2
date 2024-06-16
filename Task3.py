import numpy as np

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector

def decrypt_message(encrypted_vector, key_matrix):
    key_matrix_inv = np.linalg.inv(key_matrix)
    decrypted_vector = np.dot(key_matrix_inv, encrypted_vector)
    decrypted_message = ''.join([
        chr(int(np.round(num.real))) for num in decrypted_vector
        if 0 <= int(np.round(num.real)) < 0x110000
    ])
    return decrypted_message

# Asking user for input message
original_message = input("Enter a message: ")
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
