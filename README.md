
# SentimentLens: Understanding Customer Sentiments in Product Reviews

## Project Overview
- Created a classifier to predict sentiment of customer reviews wither positive or negative.
- Downloaded dataset from this link https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/ and sampled data due to resource constraints
- Extracted features from text by performing typical text preprocessing method and count the occurence of words inside each reviews.
- Naive Bayes model used for classification. Simple models is used because the goal is to be able to implement MLOps.
- Build a simple interactive website hosted on Amazon Web Services. The users are able to input words and then the model will predict the sentiment of the word.

## Background
In today's online shopping world, people heavily rely on product reviews to decide what to buy. Businesses need to make sense of all these reviews to understand what customers like and dislike about their products. Sentiment analysis, a part of data science, helps in this by figuring out the emotions expressed in reviews. By using sentiment analysis, businesses can learn not just if customers are happy overall, but also what specific things they like or don't like.

The main goal of using sentiment analysis on product reviews is to get useful information from what customers are saying. It helps businesses see patterns and trends in feedback, allowing them to improve certain features or address problems. It also lets businesses be more responsive to customer concerns. So, by analyzing sentiments in product reviews, businesses can listen to their customers and make smart changes to stay competitive and better meet customer needs.

## Project Scope
For Proof-of-Concept (POC), the project scope will be:
- Text Data: **Customer Product Reviews (in 2018)** 
- Company : **Amazon**

## Installation and Setup
### Resources Used
- **Code Editor:** Visual Studio Code
- **Python Version:** 3.10.13

### Python Package and Tools Used
- **Data Manipulation:** Packages used for handling and importing dataset such as `pandas and numpy`.
- **Text Preprocessing:** Packages used for handling and importing dataset such as `nltk`.
- **Natural Language Processing Model:** Packages that were used to generate the forecast model such as `scikit-learn`, etc.
- **Model Tracking:** Packages used for model tracking such as `mlflow`.
- **Model Deployment:** Packages used for model deployment through web application such as `flask and docker`.
- **Containerization:** Tools used for containerized the project such as `docker`.
- **Website Server:** Cloud Services used for hosting website server such as `Amazon Web Service`.

For running the application locally there are two ways: using Python or using Docker. But first, you have to clone this project.
- Using Python
```bash
  conda install -n <environment_name> python==3.10.13
  conda activate <environment_name>
  cd customer-product-reviews-sentiment-classifier
  pip install -r requirements.txt
  python app.py
```
- Using Docker (run the command and access the IP address)
```bash
  docker build -t sentiment-classification-app .
  docker run -p 8080:8080 sentiment-classification-app
```

## Data
### Data Columns
The data consists of 11 columns
- reviewerID (ID of the reviewer)
- asin (ID of the product)
- reviewerName (name of the reviewer)
- vote (helpful votes of the review)
- style (a disctionary of the product metadata)
- reviewText (text of the review)
- overall (rating of the product)
- summary (summary of the review)
- unixReviewTime (time of the review in unix time)
- reviewTime (time of the review in raw format)
- image (images that users post after they have received the product)
### Data Gathering
The data are downloaded from this link https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/ and sampled based on the review reting so that the data are balanced.
### Data Labeling
Assigning reviews with a label of:
- 1 if the rating (`overall`) is above or equal to 3 
- 0 if the rating below 3.
### Data Preparation
Perform text preprocessing on the raw text (`reviewText`) start from:
- Normalizing text by lower case all letters
- Tokenize words 
- Remove stop words and punctuations, 
- Lemmatize words
- Combine words into one text for prediction
### Feature Extraction
For feature extracton it is just counting the occurence of the words inside the preprocessed text and use it as an input to the model. 

## Modelling
Naive Bayes clasifier is used. For modelling we split the data before hand so that the proportion will be 80% training set and 20% test set. The model learn from the training set and test set will be used to evaluate model performance.

## Evaluation and Results

To assess the performance of our Naive Bayes classifier model, we used a straightforward method for classification, which includes the following metrics:

- Precision: This tells us the percentage of correctly identified positive sentiment review out of text that are identified as positive sentiment by the model. In simple terms, it measures how accurate our model is when it claims to have found text with positive sentiment.
- Recall: This shows the percentage of correctly identified positive sentiment review out of the total number of actual positive sentiment reviews that were actually present in the text. In simpler terms, it measures how well our model captures all actual positive sentiment reviews.
- F1-Score: This is a combination of both Precision and Recall. It gives us an overall measure of the model's performance by considering both false positives and false negatives. It's a balanced way to evaluate how well our model is performing.

## Deployment
To deploy the machine learning model through a website, I utilize Flask, a lightweight web framework for Python. The Flask application serves as the backbone of the website, handling user requests and interfacing with the machine learning model. Users input their text via a text box on the website's frontend and click the "Predict" button, which triggers an HTTP post to the Flask backend. The backend processes the input from text preprocessing, feature extraction, and model prediction. After containerizing the Flask application using Docker, I host it on an Amazon EC2 instance. This setup ensures scalability and reliability, allowing users to access the sentiment analysis service seamlessly. The backend returns the sentiment classification result alongside with the raw input text to the frontend for display, completing the streamlined process.

I implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions. This pipeline automates the process of building, and deploying the Flask application. Whenever code updates are pushed to the GitHub repository, GitHub Actions automatically trigger the CI/CD pipeline.The pipeline begins by building the Docker image of the Flask application. Once the image is built successfully, it is tagged and pushed into the Amazon Elastic Container Registry (ECR). Then, EC2 instance hosting the website pulls the latest Docker image from the ECR. The updated image is then deployed on the EC2 instance and update the website with the latest changes.

## Development in Future
- [ ]  Improve Documentation
- [ ]  Utilize word embedding for sentiment classification
- [ ]  Create an API for the model prediction