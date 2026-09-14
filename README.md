# Bangalore House Prices Prediction

This is an end-to-end Machine Learning project that predicts the real estate house prices in Bangalore, India. 

## Project Architecture
The project consists of three main parts:
1. **Machine Learning Model (`/model`)**: 
   - A Jupyter notebook used for data cleaning, feature engineering, outlier removal, and model building using Scikit-Learn.
   - The final model is trained on the Bangalore home prices dataset and exported as a pickle file (`banglore_home_prices_model.pickle`).
2. **Python Flask Server (`/server`)**: 
   - A backend server built with Flask that serves the exported ML model.
   - It exposes HTTP endpoints for the client application to fetch the list of locations and predict house prices based on user inputs.
3. **Web Client (`/client`)**: 
   - A frontend web interface built with HTML, CSS, and vanilla JavaScript. 
   - It allows users to input house features (square footage, BHK, bathrooms, location) and displays the predicted price by interacting with the Flask backend API.

## Technologies Used
- **Data Science**: Python, Pandas, Numpy, Matplotlib, Scikit-Learn, Jupyter Notebook
- **Backend Server**: Python, Flask
- **Frontend Client**: HTML, CSS, JavaScript

## Setup Instructions

### 1. Backend Server Setup
1. Navigate to the `server` directory:
   ```bash
   cd server
   ```
2. Create and activate a Python virtual environment (optional but recommended).
3. Install the required dependencies (Flask, numpy, scikit-learn, etc.).
4. Start the Flask server:
   ```bash
   python server.py
   ```
   The server will start running and listening for requests on port 5000.

### 2. Frontend Client Setup
1. Navigate to the `client` folder.
2. Simply open the `app.html` file in your preferred web browser. 
3. Ensure the Flask server is running in the background so the frontend can successfully make API calls to fetch locations and predict prices.

## Dataset
The dataset used in this project is the **Bengaluru House price data**, which contains features like area type, availability, location, size, society, total square footage, number of bathrooms, balconies, and the target price.

## Author
[7sam-l](https://github.com/7sam-l)
