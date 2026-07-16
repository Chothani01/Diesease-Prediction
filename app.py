import streamlit as st
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input


import numpy as np
from PIL import Image
from prompt_template import prompt 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b") 

MODEL_PATH = "Model//best_crop_disease_model_clean.keras"

model = load_model(MODEL_PATH, compile=False)

class_name=['apple scab','apple black rot','cedar apple rust','apple healthy','blueberry healthy','cherry powdery mildew','cherry healthy','corn cercospora leaf gray leaf spot','corn common rust','corn northern leaf blight','corn healthy','grape black rot','grape black measles','grape leaf blight','grape healthy','orange haunglongbing',
      'peach bacterial spot','peach healthy','pepper bell Bacterial spot','pepper bell healthy','potato early blight','potato late blight','potato healthy','raspberry healthy','soybean healthy','squash powdery mildew','strawberry leaf scotch','strawberry healthy','tomato bacterial spot','tomato early blight','tomato late blight','tomato leaf mold','tomato septoria leaf spot','tomato spider mites two spotted spider mite',
      'tomato target spot','Tomato yellow leaf curl virus','tomato mosaic virus','tomato healthy']

st.set_page_config(page_title='Image class', layout='centered')

st.markdown("This application will try to give you a classification of your image its build based on vanila CNN architecture.")

st.sidebar.title("Upload your image")
upload_file = st.sidebar.file_uploader('Choose your image', type=['jpg', 'jpeg', 'png'])

if st.sidebar.button('Upload'):
    img = Image.open(upload_file).convert('RGB')
    st.image(img, caption='Your image')
    resized_img = img.resize((224, 224))
    
    img_array = image.img_to_array(resized_img)
    image_batch = np.expand_dims(img_array, axis=0)
    preprocessed_input = preprocess_input(image_batch)
    
    prediction = model.predict(preprocessed_input)   
    prediction_class = class_name[np.argmax(prediction)]
    
    chain = prompt | llm
    
    output = chain.invoke({'disease_name': prediction_class})
    
    st.markdown(output.content)