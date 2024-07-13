# NLP Model for Spam Detection with Deployment on Heroku

## Description
This project focuses on building and deploying a Natural Language Processing (NLP) model to detect spam messages. The main objective is to classify messages as spam or not spam using machine learning techniques. The model is built using Python and leverages various libraries and tools to preprocess the data, train the model, and deploy the application on Heroku.

## Project Structure
The project consists of the following components:

1. **Data Preprocessing and Model Training**:
    - **Dataset**: The `spam.csv` file contains the dataset used for training the model. It includes messages labeled as 'spam' or 'ham' (not spam).
    - **Preprocessing**: The dataset is cleaned and preprocessed to convert text data into a format suitable for model training.
    - **Model Training**: A machine learning model is trained using the preprocessed data. The trained model is saved as `nlp_model.pkl` for later use.

2. **Model Deployment**:
    - **App**: The `app.py` file contains the code for deploying the trained model as a web application using Flask. The application provides an interface for users to input messages and receive predictions on whether the message is spam or not.
    - **Transform**: The `transform.pkl` file contains the data transformation pipeline used during preprocessing, ensuring consistency between training and deployment.

3. **Requirements**:
    - The `requirements.txt` file lists all the dependencies required to run the project. Key libraries include Flask, scikit-learn, numpy, and nltk.

4. **Deployment on Heroku**:
    - The project is configured for deployment on Heroku using a `Procfile` that specifies the command to run the web application.

## What I Have Done in the Project
1. **Data Collection and Preprocessing**:
    - Collected and cleaned the dataset.
    - Preprocessed the text data to convert it into a suitable format for model training.

2. **Model Training**:
    - Trained a machine learning model to classify messages as spam or not spam.
    - Saved the trained model and the data transformation pipeline.

3. **Application Development**:
    - Developed a Flask web application to serve the model predictions.
    - Provided an interface for users to input messages and receive predictions.

4. **Deployment on Heroku**:
    - Configured the application for deployment on Heroku.
    - Deployed the Flask application on Heroku to make it accessible online.
