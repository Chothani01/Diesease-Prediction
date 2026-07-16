# Plant Disease Prediction

A complete plant disease classification and advisory web application built with Streamlit, TensorFlow/Keras, and an LLM prompt pipeline. This project detects disease from leaf images, identifies the correct disease class, and generates actionable treatment guidance in both English and Malayalam.

## Project Summary

This project demonstrates an end-to-end machine learning application with:
- image preprocessing and classification using a pretrained CNN model,
- a simple web interface for uploading plant leaf images,
- a prompt-driven language model integration to translate raw model output into user-friendly disease descriptions,
- bilingual output for improved local usability.

## Key Features

- **Image-based disease classification** using a pretrained Keras model (`Model/vgg16model.h5`).
- **Support for multi-class plant disease detection** across 38 crop/disease categories.
- **Streamlit UI** for easy image upload and live prediction.
- **Bilingual advisory output** in English and Malayalam using `langchain_groq`.
- **Simple deployment flow** with a local Streamlit app.

## Resume-Ready Highlights

- Developed a production-style machine learning application for agricultural disease detection.
- Implemented image preprocessing, model inference, and result rendering in a Streamlit web app.
- Integrated a prompt-based LLM pipeline to convert model predictions into detailed disease insights.
- Supported bilingual output, enhancing accessibility for regional users.
- Organized dataset and model assets for reproducible inference and future training.

## Project Structure

- `app.py` - Main Streamlit app that loads the model, accepts image uploads, makes predictions, and displays advisory text.
- `prompt_template.py` - Prompt template for generating disease descriptions in English and Malayalam.
- `Model/vgg16model.h5` - Pretrained CNN model for leaf disease classification.
- `New_Plant_Diseases_Dataset/` - Dataset folders for training and validation images.
- `train.ipynb` - Notebook for exploring and training the model (if available).
- `.env` - Environment file for API keys and configuration.

## Dataset

The dataset contains labeled leaf images for multiple crops and disease states, organized into training and validation folders. It includes both diseased and healthy leaf images for crops such as:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

## Technical Stack

- Python
- Streamlit
- TensorFlow / Keras
- NumPy
- Pillow
- LangChain Groq integration
- dotenv for environment configuration

## Installation

1. Create and activate a Python environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install required packages:

```bash
pip install streamlit tensorflow numpy pillow python-dotenv langchain-groq
```

3. Ensure the pretrained model file exists at `Model/vgg16model.h5`.

4. Add any necessary API keys to `.env` if you plan to use the LLM integration.

## Running the App

From the project root folder, run:

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`). Upload a leaf image using the sidebar, and the app will display the predicted disease class and bilingual guidance.

## Application Flow

1. User uploads an image using the Streamlit sidebar.
2. `app.py` loads the image and resizes it to `224x224`.
3. The image is normalized and converted into a model input tensor.
4. The pretrained CNN model predicts a disease label.
5. The label is passed into `prompt_template.py`.
6. The language model returns a structured description and mitigation advice in English and Malayalam.
7. The app displays the results to the user.

## Notes and Recommendations

- The app is currently configured for inference only; retraining requires additional model development.
- The prompt template is designed to deliver a consistent bilingual format and can be extended for additional languages.
- For production deployment, consider packaging the app with Docker or deploying to a cloud service.

## Future Improvements

- Add support for real-time camera capture.
- Add confidence scores for model predictions.
- Add a full training script to retrain the model from scratch.
- Improve UI/UX with a cleaner design and image history.
- Add a fallback response when the LLM is unavailable.
