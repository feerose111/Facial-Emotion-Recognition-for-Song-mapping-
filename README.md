# Facial Emotion Recognition and Song Mapping

This project combines computer vision and machine learning techniques to recognize facial emotions and map them to suitable songs. By analyzing facial expressions using a Convolutional Neural Network (CNN), the system identifies the user's emotional state and suggests songs that match the mood.

---

## Features

- **Facial Emotion Recognition:**
  - Detects emotions such as happiness, sadness, anger, surprise, and neutrality.
  - Uses a CNN model trained on a labeled dataset of facial images.

- **Song Mapping:**
  - Maps the detected emotion to a curated playlist of songs.
  - Dynamically adjusts song suggestions based on real-time facial input.

---

## Project Workflow

1. **Face Detection:**
   - Detects and extracts faces from images or webcam video using a pre-trained face detection model e.g. Haar cascades.

2. **Emotion Recognition:**
   - Processes the detected face using a trained CNN to classify emotions.

3. **Song Mapping:**
   - Maps the recognized emotion to an appropriate playlist or mood-based song recommendation.

---

## Installation

### Prerequisites

- Python 3.7+
- Libraries:
  - OpenCV
  - TensorFlow/Keras
  - NumPy
  - Pandas
  - Matplotlib

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/feerose111/Facial-Emotion-Recognition-for-Song-mapping-.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd Facial-Emotion-Recognition-for-Song-mapping-
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the application.
2. Allow access to your webcam.
3. The system will detect your face and analyze your emotions.
4. Based on the detected emotion, a song recommendation will appear.

---

## Dataset

- **Facial Emotion Dataset:**
  - The model is trained on datasets like FER2013 or other labeled datasets of facial expressions.

- **Song Database:**
  - A curated dataset of songs categorized by mood or emotion.

---

## Model Architecture

- **Convolutional Neural Network (CNN):**
  - Multiple convolutional layers with ReLU activation.
  - Max pooling layers to reduce dimensionality.
  - Fully connected layers for emotion classification.

---

## Future Enhancements

- Multi-emotion recognition to handle mixed emotions.
- Expand song database with user feedback.
- Mobile application version for broader accessibility.

---
