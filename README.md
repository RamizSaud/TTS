Got it! Here's the full `README.md` file with all the necessary content, including the additional details you mentioned:

```
# Urdu Text-to-Speech (TTS) System

This repository contains a custom Urdu Text-to-Speech (TTS) system, trained using the Tacotron2 model, based on a dataset created from YouTube audiobooks. The system generates high-quality Urdu speech from text.

# Video Demonstration
<a href="https://youtube.com/shorts/VevL_4ImpCo?feature=share"><img src="https://img.youtube.com/vi/VevL_4ImpCo/0.jpg" width="100%"/></a>

## Requirements

This project requires Python 3.7 and pip to install dependencies.

1. **Python version**: 3.7
2. **Install dependencies**: 
   To install the required libraries, run:
   ```bash
   pip install -r requirements.txt
   ```

## Directory Structure

The project is organized into the following folders:

### 1. **Creating Dataset Folder**
   - This folder contains scripts and processes for creating the custom dataset from YouTube audiobooks. It includes both the audio files and the corresponding text data.

### 2. **Training Folder**
   - This folder holds the training scripts, where the Tacotron2 model is trained on the custom dataset for Urdu TTS. It also includes the configuration files and preprocessed data used for training.

### 3. **Inference Folder**
   - This folder contains the inference scripts used for generating speech from text using the trained model. You can input Urdu text here and receive the corresponding audio output.

### 4. **App Folder**
   - The app folder contains the application logic for integrating the trained TTS model into an app. This is the folder where you can find the front-end and back-end parts of the TTS system.

## Steps to Use

### 1. **Creating the Dataset**
   - Gather YouTube audiobooks or any other suitable Urdu audio content.
   - Preprocess the audio and text files to match the format required for training (audio/text pairs).
   - Place the dataset in the appropriate folder and run the dataset creation scripts.

### 2. **Training the Model**
   - Use the training scripts in the `Training` folder to train the Tacotron2 model on the custom Urdu dataset. The model will learn to generate speech from the input text based on the audio/text pairs.

### 3. **Running Inference**
   - Once the model is trained, go to the `Inference` folder.
   - Provide an Urdu text input, and run the inference script to generate audio using the trained model.

### 4. **Integrating into the App**
   - To integrate the TTS model into an application, use the files in the `App` folder. This includes app-specific logic, such as voice output integration, UI, and API calls to the trained model.

## Acknowledgements

- Tacotron2 model for text-to-speech.
- Dataset creation using YouTube audiobooks.
```

You can copy this entire content and paste it into your text editor for the `README.md` file.
