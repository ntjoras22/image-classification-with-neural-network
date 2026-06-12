# CIFAR-10 Image Classification

A deep learning project for classifying images from the CIFAR-10 dataset using Convolutional Neural Networks (CNN) built with TensorFlow and Keras.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project implements an image classification system using a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset. The model can identify 10 different object categories with high accuracy.

The project includes:

- **Data Loading & Preprocessing**: Loads CIFAR-10 dataset and normalizes pixel values
- **Model Training**: Trains a CNN model on the training dataset
- **Visualization**: Displays sample images with predictions
- **Inference**: Predicts class labels for custom images

---

## ✨ Features

- ✅ Full pipeline for image classification
- ✅ CNN model with multiple convolutional layers
- ✅ Data augmentation and normalization
- ✅ Model saving and loading capability
- ✅ Support for custom image predictions
- ✅ Visualization of training samples
- ✅ Performance metrics (accuracy and loss)

---

## 📊 Dataset

**CIFAR-10** (Canadian Institute For Advanced Research)

- **Total Images**: 60,000
- **Training Set**: 50,000 images
- **Testing Set**: 10,000 images
- **Image Size**: 32×32 pixels (RGB)
- **Classes**: 10 object categories
  - Airplane
  - Automobile
  - Bird
  - Cat
  - Deer
  - Dog
  - Frog
  - Horse
  - Ship
  - Truck

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/image_classification.git
cd image_classification
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install opencv-python numpy matplotlib tensorflow
```

---

## 💻 Usage

### Training the Model

Run the script to load data, train the model, and save it:

```bash
python main.py
```

This will:

1. Load the CIFAR-10 dataset
2. Display 16 sample images with their labels
3. Build and train the CNN model
4. Save the trained model as `image_classification.keras`

### Predicting on Custom Images

The script includes a prediction section. To classify your own image:

1. Place your image in the project folder (e.g., `deer.jpg`)
2. Update the filename in `main.py`:
   ```python
   img = cv.imread('your_image.jpg')
   ```
3. Run the script:
   ```bash
   python main.py
   ```

The script will display your image and print the predicted class.

---

## 📁 Project Structure

```
image_classification/
│
├── main.py                          # Main script for training and inference
├── image_classification.keras       # Trained model (generated after running)
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore file
├── README.md                        # This file
└── sample_images/                   # (Optional) Folder for custom images
```

---

## 🧠 Model Architecture

The CNN model consists of:

```
Input Layer (32×32×3)
    ↓
Convolutional Block 1: 32 filters, 3×3 kernel
    ↓
MaxPooling Layer: 2×2 pool size
    ↓
Convolutional Block 2: 64 filters, 3×3 kernel
    ↓
MaxPooling Layer: 2×2 pool size
    ↓
Flatten Layer
    ↓
Dense Layer: 64 units, ReLU activation
    ↓
Dropout Layer: 0.5 rate
    ↓
Output Layer: 10 units, Softmax activation
    ↓
Predictions (10 classes)
```

**Parameters**:

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Metric: Accuracy

---

## 📈 Results

After training on the CIFAR-10 dataset:

- **Training Accuracy**: High (typically 80-90%)
- **Testing Accuracy**: Competitive (typically 70-85%)
- **Model Size**: Approximately 2-5 MB

_Results may vary depending on training parameters and epochs._

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📚 Resources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Keras Documentation](https://keras.io/)
- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [CNN Fundamentals](https://en.wikipedia.org/wiki/Convolutional_neural_network)

---

## 🆘 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'cv2'`

**Solution**: Ensure virtual environment is activated and install dependencies:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: Model file too large to push to GitHub

**Solution**: The `.keras` model files are excluded from Git by default. Train the model locally using `python main.py`.

### Issue: Custom image prediction fails

**Solution**:

- Ensure image is in the project directory
- Check image format (JPG, PNG, etc.)
- Verify file path in `main.py`

---

## 📧 Contact

For questions or issues, please open an issue on [GitHub Issues](https://github.com/YOUR_USERNAME/image_classification/issues).

---

**Happy Learning! 🚀**
