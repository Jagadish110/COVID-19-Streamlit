# 🦠 COVID-19 Detection Using Chest X-Rays with CNN

This project applies Convolutional Neural Networks (CNN) to detect COVID-19 from chest X-ray images. It demonstrates the use of deep learning in healthcare for automated diagnosis.

---

## 🩺 How This Helps Healthcare

Early and accurate detection of COVID-19 is crucial in preventing the spread and ensuring timely treatment. This AI-powered solution:

- Reduces the workload on radiologists by automating diagnosis.
- Enables rapid screening in areas with limited access to PCR tests.
- Assists in triaging patients in critical healthcare environments.
- Can be integrated into mobile or web apps for real-time diagnostics in remote regions.

By using chest X-rays, which are readily available in most medical facilities, this system provides a fast, low-cost, and scalable way to detect COVID-19.

---

## 🖼️ Live Demo Interface

Here's what the interface looks like when deployed:

![Screenshot 2025-06-29 142134](https://github.com/user-attachments/assets/bc98ecc9-f8b0-4bad-8246-ae45be57c42e)


## 📌 Project Overview

- **Objective**: Classify chest X-rays as COVID-19 Positive or Negative.
- **Dataset**: Public datasets such as COVIDx or the Kaggle COVID-19 Radiography Database.
- **Interface**: Built using Streamlit for easy user interaction.

---

## 🧠 Model Summary

- CNN with Conv2D, MaxPooling2D, Dense layers
- Activation: ReLU, Softmax
- Loss: Categorical Crossentropy
- Optimizer: Adam
- Metric: Accuracy

---

## 📁 Dataset Structure

dataset/
├── train/
│ ├── covid/
│ └── normal/
├── val/
│ ├── covid/
│ └── normal/
└── test/
├── covid/
└── normal/





