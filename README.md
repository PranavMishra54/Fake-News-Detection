# 📰 Fake News Detection

A Machine Learning-based web application that classifies news articles as **Real** or **Fake** using **Natural Language Processing (NLP)** techniques. The project leverages **TF-IDF Vectorization** and a **Support Vector Machine (SVM) Classifier** to analyze news content and predict its authenticity through an interactive Streamlit interface.

---

## 🚀 Features

* Detects whether a news article is **Real** or **Fake**
* User-friendly web interface built with Streamlit
* Text preprocessing and feature extraction using NLP
* TF-IDF Vectorization for text representation
* SVM Classifier for accurate prediction
* Instant classification results
* Lightweight and easy to deploy

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Pickle

---

## 📂 Project Structure

```text
Fake-News-Detection/
│
├── app.py                 # Streamlit application
├── model.pkl              # Trained SVM model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Dependencies
├── README.md              # Documentation
```

---

## 🧠 Model Details

This project uses a **Support Vector Machine (SVM) Classifier**, a powerful supervised learning algorithm widely used for text classification tasks.

### Text Processing Pipeline

1. User enters a news article.
2. Text preprocessing is applied.
3. TF-IDF Vectorizer converts text into numerical feature vectors.
4. The trained SVM model analyzes the features.
5. The model predicts whether the news is **Real** or **Fake**.

### Why SVM?

* Effective for high-dimensional text data.
* Performs well with sparse TF-IDF features.
* Strong accuracy for binary classification problems.
* Computationally efficient for medium-sized datasets.

---


## 📊 Dataset

The model is trained on a labeled fake news dataset containing both real and fake news articles. The dataset undergoes preprocessing and feature extraction before training the SVM classifier.

Typical preprocessing steps include:

* Lowercasing text
* Removing punctuation and special characters
* Removing stopwords
* TF-IDF feature extraction

---

## 📈 Machine Learning Workflow

```text
News Article
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
SVM Classifier
      │
      ▼
Real News / Fake News
```

---

## 💡 Example Usage

1. Launch the Streamlit application.
2. Paste or type a news article into the text box.
3. Click the prediction button.
4. View the classification result.

---

## 🔮 Future Improvements

* Integration of Deep Learning models (LSTM, BERT)
* Multi-language fake news detection
* Confidence score for predictions
* News source credibility analysis
* FastAPI backend deployment
* Real-time news verification

---

## 👨‍💻 Author

**Pranav Mishra**

B.Tech Information Technology
Madan Mohan Malaviya University of Technology (MMMUT), Gorakhpur

Interests:

* Artificial Intelligence
* Machine Learning
* Data Science
* Full-Stack Development
* NLP Applications
