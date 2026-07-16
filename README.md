# 🌿 Plant Disease Detection using EfficientNetB0

An AI-powered web application that detects plant diseases from leaf images using **EfficientNetB0** and provides **AI-generated disease descriptions and treatment recommendations** using **LangChain + Groq LLM**.

---

## 📌 Features

- 🌱 Detects diseases from plant leaf images
- 🧠 Uses EfficientNetB0 Transfer Learning
- 📷 Upload JPG, JPEG, or PNG images
- ⚡ Fast predictions using TensorFlow/Keras
- 🤖 AI-generated disease explanation and treatment suggestions using Groq LLM
- 🌐 User-friendly Streamlit interface

---

## 🪴 Supported Plants

The model can classify **38 classes**, including:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Pepper Bell
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

including healthy and diseased leaves.

---

## 🛠 Tech Stack

- Python
- TensorFlow
- Keras
- EfficientNetB0
- Streamlit
- LangChain
- Groq API
- Pillow
- NumPy

---

## 📂 Project Structure

```
Plant-Disease-Detection/
│
├── Model/
│   └── best_crop_disease_model_clean.keras
│
├── app.py
├── prompt_template.py
├── requirements.txt
├── train_EfficientNet.ipynb
├── README.md
└── images/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser at

```
http://localhost:8501
```

---

## 🧠 Model

- Base Model: EfficientNetB0
- Input Size: 224 × 224
- Transfer Learning
- Data Augmentation
- Categorical Classification
- ImageNet Pretrained Weights

---

## 📸 How It Works

1. Upload a plant leaf image.
2. Image is resized to **224×224**.
3. EfficientNet preprocessing is applied.
4. The trained model predicts the disease.
5. LangChain + Groq generates:
   - Disease description
   - Symptoms
   - Causes
   - Prevention
   - Treatment recommendations

---

## 📊 Dataset

The model was trained on the **PlantVillage Dataset**, containing healthy and diseased plant leaf images across multiple crop species.

Dataset Link:
https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

---

## Future Improvements

- Mobile Application
- Multi-language Support
- Disease Severity Estimation
- Fertilizer Recommendation
- Weather-based Disease Alerts
- Camera-based Real-time Detection

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---
