# 🚧 Road Damage Object Detection using YOLOv8 & Streamlit

## 📌 Project Overview

This project aims to automatically detect and classify different types of road damage using YOLO object detection models.

The system can identify road defects from images and visualize detections using bounding boxes and confidence scores through an interactive Streamlit application.

---

## 🎯 Damage Classes

The model detects the following road damage categories:

- Longitudinal Crack
- Transverse Crack
- Alligator Crack
- Other Corruption
- Pothole

---

## 📊 Exploratory Data Analysis (EDA)

The dataset was analyzed to understand:

- Class distribution
- Bounding box distribution
- Bounding box width and height
- Bounding box area
- Aspect ratio analysis
- Small, medium, and large object distribution
- Visual inspection of annotated images

---

## 🤖 Models Trained

Two YOLO models were trained and evaluated:

- YOLOv8n
- YOLOv8s

---

## 📈 Model Comparison

| Model | Precision | Recall | mAP50 | mAP50-95 | FPS | Model Size (MB) |
|---------|---------|---------|---------|---------|---------|---------|
| YOLOv8n | 0.558 | 0.503 | 0.503 | 0.248 | 51.26 | 5.96 |
| YOLOv8s | 0.587 | 0.522 | 0.529 | 0.269 | 43.83 | 21.48 |

### ✅ Selected Model

YOLOv8s was selected as the final model because it achieved better detection performance across all evaluation metrics while maintaining a reasonable inference speed.

---

## 🚀 Deployment

A Streamlit web application was developed to:

- Upload road images
- Detect road damages automatically
- Display bounding boxes
- Show confidence scores for detected objects

---

## 🛠️ Technologies Used

- Python
- YOLOv8
- Ultralytics
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Streamlit

---

## 📂 Project Structure

```text
Road-Damage-Object-Detection/
│
├── Deployment.py
├── Road_Damage_Detection.ipynb
├── requirements.txt
├── README.md
├── .gitignore
│
└── Results/
```

---

## 📸 Sample Results

Add screenshots of:

- Detection results
- Streamlit application
- Model comparison
- Dataset analysis

---

## 🔗 GitHub Repository

Repository Link:

https://github.com/YoussefAlaa10-AI/Road-Damage-Object-Detection

---

## 👨‍💻 Author

Youssef Alaa

AI Engineer | Data Scientist | Data Analyst
