import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from sklearn.decomposition import PCA

image = imread('image.png')

plt.imshow(image)
plt.title('Початкове кольорове зображення')
plt.show()

image_shape = image.shape
print("Розміри зображення (height, width, channels):", image_shape)

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.imshow(image_gray, cmap='gray')
plt.title('Чорно-біле зображення')
plt.show()

image_gray_shape = image_gray.shape
print("Розміри чорно-білого зображення:", image_gray_shape)

pca = PCA()
pca.fit(image_gray)

cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print("Кількість компонент для покриття 95% варіації:", components_95)

plt.plot(cumulative_variance)
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Variance Explained')
plt.title('Cumulative Variance Explained by PCA Components')
plt.axhline(y=0.95, color='r', linestyle='--')
plt.axvline(x=components_95, color='r', linestyle='--')
plt.show()

pca_limited = PCA(n_components=components_95)
image_gray_transformed = pca_limited.fit_transform(image_gray)

image_gray_reconstructed = pca_limited.inverse_transform(image_gray_transformed)

plt.imshow(image_gray_reconstructed, cmap='gray')
plt.title(f'Реконструйоване чорно-біле зображення (95% варіації)')
plt.show()

components_list = [10, 20, components_95, 50, 100]

for n_components in components_list:
    pca = PCA(n_components=n_components)
    image_transformed = pca.fit_transform(image_gray)
    image_reconstructed = pca.inverse_transform(image_transformed)

    plt.imshow(image_reconstructed, cmap='gray')
    plt.title(f'Реконструйоване зображення (n_components={n_components})')
    plt.show()
