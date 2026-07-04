Advert Sales Predictor

A Streamlit web app that predicts sales based on advertising spend across TV, Radio, Social Media, and Influencer marketing.

Overview

Businesses invest heavily in advertising across multiple channels but often struggle to quantify how that spend translates into sales. This project explores the relationship between advertising expenditure (TV, Radio, Social Media) and Influencer type on sales, using a Linear Regression model trained on 4,572 records. The trained model is deployed in a Streamlit app where users can input hypothetical ad spend and see a predicted sales value.

Dataset

The dataset [(AdvertAndSales.csv)](https://github.com/Osabhue-Mathew24/Advert_and_Sales/blob/main/AdvertAndSales.csv) contains 4,572 rows with the following columns:


TV — advertising expenditure on TV
Radio — advertising expenditure on radio
Social Media — advertising expenditure on social media
Influencer — category of influencer used (e.g., Mega, Micro)
Sales — the target variable


Rows with missing values were dropped during preprocessing, leaving a clean dataset for training.

Model


Algorithm: Linear Regression (scikit-learn)
Train/test split: 80/20 (3,636 training rows, 910 test rows)
Performance:

R² on training set: 0.999
R² on test set: 0.999



The Influencer categorical column was label-encoded before training, and the fitted encoder was saved separately (Influencer_encoder.pki) so the same encoding can be applied to new input in the app


Given the very high R² on both train and test sets, advertising spend and influencer type explain sales almost entirely in this dataset — worth noting as a possible sign of a small/synthetic dataset rather than assuming it as a benchmark for real-world ad spend data.

Features


Custom-styled title and header using Streamlit's HTML/CSS support
A "Background of Study" section explaining the purpose of the analysis directly in the app
Displays the full dataset used for the analysis in an interactive table
Sidebar inputs (defaulting to each column's median value) for TV, Radio, and Social Media advertising expenditure
Sidebar dropdown to select influencer type from the dataset's actual categories
Shows the user's input as a table before prediction
Encodes the influencer input using the saved encoder, then predicts sales on button click


Tech Stack


Python
Streamlit — web app interface
Pandas / NumPy — data handling
Scikit-learn — Linear Regression model, train/test split, R² and MAE evaluation, label encoding
Seaborn / Matplotlib — correlation heatmap during exploratory analysis
Joblib — saving/loading the trained model and encoder
Jupyter Notebook — exploratory analysis and model development (AdSales.ipynb)


Project Structure

Advert_and_Sales/
├── AdSales.py              # Streamlit app
├── AdSales.ipynb            # Data exploration and model training notebook
├── AdvertAndSales.csv        # Dataset
├── advertmodel.pki           # Trained regression model
├── Influencer_encoder.pki    # Encoder for the influencer category
├── requirements.txt           # Project dependencies


How It Works


The dataset is loaded and displayed in the app for reference
The user enters TV, Radio, and Social Media advertising spend (defaulting to each column's median), and selects an influencer type from the sidebar
The entered values are shown back to the user as a table before prediction
The influencer type is transformed using the saved label encoder (Influencer_encoder.pki)
On clicking "Push to predict the Sales," the processed input is passed into the trained Linear Regression model (advertmodel.pki)
The predicted sales value is displayed on the screen


Future Improvements


Try additional models (e.g., Random Forest, Ridge/Lasso Regression) and compare performance against the current Linear Regression baseline
Display the R² / MAE metrics directly in the app for transparency
Add data visualizations (e.g., the correlation heatmap from the notebook) within the app itself
Investigate why R² is close to 1.0 — check for potential data leakage or overly simplified/synthetic data generation
Deploy the app publicly (e.g., Streamlit Community Cloud) and link it here


Author

Matthew Osabhue Iyasele

Email: mathewiyasele@gmail.com
