# 🧠 Deep Learning-Based Alzheimer’s Disease Detection and Classification Using VGG-16 CNN

This project focuses on using **Deep Learning** to detect and classify **Alzheimer’s Disease** from MRI brain images using the **VGG-16 Convolutional Neural Network**. It helps in early diagnosis by classifying brain scans into different stages of dementia automatically and efficiently.

## 📘 Project Overview
Alzheimer’s Disease (AD) is a neurodegenerative disorder that affects memory and cognitive abilities. Early detection can significantly improve treatment outcomes.  
This project uses a **VGG-16 CNN model** trained with MRI datasets to classify images into:
- Non-Demented  
- Very Mild Demented  
- Mild Demented  
- Moderate Demented  

**Accuracy Achieved:** 89.80%

## 🎯 Objectives
- Automate the detection of Alzheimer’s Disease using MRI images.  
- Apply **VGG-16** for high accuracy in classification.  
- Provide a simple web interface for easy prediction and visualization.  

## 🧩 Methodology
1. **Dataset Preparation:** MRI images collected from Kaggle.  
2. **Preprocessing:** Image resizing, normalization, and augmentation.  
3. **Model:** Transfer learning using **VGG-16 CNN** with fine-tuning.  
4. **Training:** Optimized using Adam optimizer and categorical cross-entropy loss.  
5. **Testing:** Model validated and evaluated using accuracy and confusion matrix.  

## ⚙️ Tools and Technologies
- **Programming Language:** Python  
- **Frameworks:** TensorFlow, Keras, Flask  
- **Frontend:** HTML, CSS  
- **Libraries:** NumPy, Pandas, Matplotlib  
- **Editor:** Jupyter Notebook / VS Code  

## 💻 Implementation
- Developed a CNN model (`vgg16_model.keras`) for Alzheimer’s detection.  
- Flask backend handles image uploads and predictions.  
- Frontend built using HTML and CSS for user interaction.

**Files:**
app.py
/templates
├── index.html
├── predict.html
├── result.html
/static
└── style.css
/model
└── vgg16_model.keras

## 📊 Results
| Metric | Value |
|--------|--------|
| Training Accuracy | 89.80% |
| Validation Accuracy | 77.77% |
| Testing Accuracy | ~88% |

**Output Classes:**
- Healthy Brain  
- Very Mild Dementia  
- Mild Dementia  
- Moderate Dementia  

## 👩‍💻 Author By
  Janani Raja  

## 🧾 Conclusion
This project demonstrates how **VGG-16 CNN** can effectively classify Alzheimer’s stages from MRI scans.  
It reduces manual diagnostic effort and supports early, accurate detection to improve clinical decision-making.


