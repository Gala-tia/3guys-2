import numpy as np
image = np.random.randn(1, 3, 32, 32)
print(image.shape)
x = np.random.randn(1, 3, 32, 32)
y = np.vstack((x, image))
print(y.shape)
z = np.vstack((y, y))
print(z.shape)
