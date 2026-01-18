**Heart Disease Prediction System**

This project implements a Heart Disease Prediction system using machine learning. The model analyzes critical health parameters such as age, blood pressure, cholesterol levels, and other medical factors to predict the likelihood of a person having heart disease.

A simple user interface is created using Flask in PyCharm, where users can enter patient details and get instant predictions. The focus of this project is on developing an accurate machine learning model rather than advanced UI design.

“Since the dataset is small (~300 samples) and the problem is binary medical classification,
I used Logistic Regression as a baseline, SVM for margin-based learning,
and Random Forest as a bagging-based ensemble to reduce overfitting.
Boosting was avoided because it may overfit on small medical datasets.”

Logistic Regression provides a balanced performance with good recall, higher overall accuracy, and better interpretability, which is crucial for medical decision-support systems. Logistic Regression achieved the best balance between accuracy (81.6%), recall, and false negative rate. Since medical datasets prioritize interpretability and minimizing false negatives by adjusting the probability threshold, Logistic Regression was selected as the final model.

 Key Features

* Predicts the risk of heart disease based on patient health data.

* Uses a trained machine learning model for reliable predictions.

* Simple and easy-to-use interface built with Flask.

 Future Improvements

* Incorporate larger datasets to improve model accuracy.

* Explore advanced machine learning algorithms for better predictions.

* Integrate real-time medical inputs for more practical use in healthcare.

The website (built using Flask and developed in PyCharm) looks like this 👇

  <img width="653" height="916" alt="image" src="https://github.com/user-attachments/assets/eef8c1b8-5954-4102-a5f3-85267a80ce84" />
