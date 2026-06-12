import numpy as np
from tensorflow.keras import datasets, layers, models

# Load and preprocess data
print("Loading CIFAR-10 dataset...")
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images / 255.0, testing_images / 255.0

# Use subset for faster training
training_images = training_images[:10000]
training_labels = training_labels[:10000]
testing_images = testing_images[:4000]
testing_labels = testing_labels[:4000]

print(f"Training samples: {len(training_images)}")
print(f"Testing samples: {len(testing_images)}")

# Build the CNN model
print("\nBuilding CNN model...")
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Display model architecture
print("\nModel Architecture:")
model.summary()

# Train the model
print("\nTraining model...")
history = model.fit(
    training_images, 
    training_labels, 
    epochs=10, 
    batch_size=128,
    validation_data=(testing_images, testing_labels),
    verbose=1
)

# Evaluate on test data
print("\nEvaluating model on test data...")
loss, accuracy = model.evaluate(testing_images, testing_labels, verbose=0)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")

# Save the trained model
print("\nSaving model...")
model.save('image_classification.keras')
print("Model saved as 'image_classification.keras'")
