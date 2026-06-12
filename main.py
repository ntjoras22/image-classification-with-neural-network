import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from tensorflow.keras import datasets,layers,models

(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images / 255.0, testing_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i][0]])

plt.show()

training_images = training_images[:10000]
training_labels = training_labels[:10000]

testing_images = testing_images[:4000]
testing_labels = testing_labels[:4000]  



model = models.load_model('image_classification.keras')
img = cv.imread('deer.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.resize(img, (32, 32))

plt.imshow(img, cmap=plt.cm.binary)

prediction = model.predict(np.array([img]) / 255.0)

print("Predicted class:", class_names[np.argmax(prediction[0])])

plt.show()