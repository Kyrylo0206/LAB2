import numpy as np

def eigenvalues(matrix):
    eigvals, eigvecs = np.linalg.eig(matrix)

    for i in range(len(eigvals)):
        eigvals = eigvals[i]
        eigvecs = eigvecs[:,i]

        left_side = np.dot(matrix, eigvecs)
        right_side = eigvals * eigvecs

        if np.allclose(left_side, right_side):
            print(
                f"Рівність виконується для власного значення {eigvals} і відповідного власного вектора {eigvecs}")
        else:
            print(
                f"Рівність НЕ виконується для власного значення {eigvals} і відповідного власного вектора {eigvecs}")

        return eigvals, eigvecs
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
eigvals, eigvecs = eigenvalues(matrix)

print("Власні значення:", eigvals )
print("Власні вектори:")
print(eigvecs)
