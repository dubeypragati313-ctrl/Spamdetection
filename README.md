# Spamdetection
An interactive Machine Learning web app built with Python and Streamlit to classify emails and SMS messages as Spam or Normal (Ham).
# 🛡️ Smart Email & SMS Spam Detector

## 📌 Project Overview
The **Smart Email & SMS Spam Detector** is a Machine Learning-powered web app designed to analyze incoming text messages and emails to determine whether they are **Spam** (phishing, promotional, scams) or **Ham** (safe/normal messages). 

Built using **Python**, **Scikit-Learn**, and **Streamlit**, this project utilizes **Natural Language Processing (NLP)** techniques like TF-IDF Vectorization to process text inputs and classify them in real-time.

---

## ✨ Key Features
- **Real-Time Classification:** Instantly detects spam or normal text with high accuracy.
- **Interactive UI:** Clean, responsive, and user-friendly interface powered by Streamlit.
- **Prediction History & Analytics:** Tracks total checks and displays live spam vs. ham count in the sidebar.
- **Sample Test Inputs:** Pre-loaded sample messages for quick testing.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Machine Learning & NLP:** Scikit-Learn (Multinomial Naïve Bayes, TF-IDF Vectorizer), Pandas, NumPy
- **Frontend / Web Framework:** Streamlit
- **Model Persistence:** Pickle

---

## 📊 Dataset
The model is trained on the standard **SMS Spam Collection Dataset**, containing labeled messages tagged as either `ham` or `spam`.
